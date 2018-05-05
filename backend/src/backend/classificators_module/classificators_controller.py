from src.backend import app, db
from flask import Blueprint, request, abort
from flask_api import status
import src.data_preparation.data_loader as dl
import src.data_visualization.data_printer as dp
import src.classificators.naive_bayes as nb
import src.classificators.svm as svm
import src.classificators.decision_tree as tree
import bson.json_util as json_util
import datetime
import pickle
import time

classificators = Blueprint('classificators', __name__)
algorithms = {
    "bayes": nb,
    "svm": svm,
    "tree": tree
}


@classificators.route('/<algorithm_name>/predict', methods=['POST'])
def get_classification(algorithm_name):
    if algorithm_name not in algorithms:
        app.logger.error("Wrong algorithm name in url")
        abort(status.HTTP_404_NOT_FOUND, "Wrong algorithm name in url")

    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST, "Missing file")

    if "with_target" not in request.form:
        app.logger.error('Missing target info')
        abort(status.HTTP_400_BAD_REQUEST, "Missing target info")

    if algorithms[algorithm_name].model is None:
        app.logger.info("Model not trained yet")
        abort(status.HTTP_406_NOT_ACCEPTABLE, "Model not trained yet")

    with_target = string_match_true(request.form["with_target"])

    file = request.files['file'].read().decode('ascii')
    file = file.splitlines()

    data, target, ids = dl.read_file(file, with_target)
    predicted = algorithms[algorithm_name].predict(data)
    accuracy = dp.get_classification_accuracy(predicted, target, inPercent=False)
    total = len(predicted)

    return_dict = {"accuracy": {k: v * 100 / total for k, v in accuracy.items()},
                   "predicted_values": dp.match_ids_with_predicted_values(ids, predicted)}

    if with_target:
        collection = db.get_collection("total_accuracy")
        collection.find_one_and_update({'_id': algorithm_name},
                                       {'$inc': {'total': total,
                                                 "tn": accuracy["tn"],
                                                 "tp": accuracy["tp"],
                                                 "fp": accuracy["fp"],
                                                 "fn": accuracy["fn"]}},
                                       upsert=True)

    collection = db.get_collection(algorithm_name + "_history")
    classifier_info = db.classifier_info.find_one({"_id": algorithm_name})
    return_dict["time"] = datetime.datetime.utcnow()
    return_dict["classifier_info"] = classifier_info
    collection.insert_one(return_dict)

    return json_util.dumps(return_dict), status.HTTP_200_OK


@classificators.route('/<algorithm_name>/train', methods=['POST'])
def train_model(algorithm_name):
    if algorithm_name not in algorithms:
        app.logger.error("Wrong algorithm name in url")
        abort(status.HTTP_404_NOT_FOUND, "Wrong algorithm name in url")

    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST, "Missing file")

    if "options" not in request.form:
        options = {}
    else:
        options = json_util.loads(request.form["options"])
        options = {k: v for k, v in options.items() if v}

    if "with_selection" not in request.form:
        app.logger.error('Missing selection info')
        with_selection = False
    else:
        with_selection = string_match_true(request.form["with_selection"])

    app.logger.info("Passed options: {}, {}".format(options, with_selection))

    file = request.files['file'].read().decode('ascii')
    file = file.splitlines()

    data, target, ids = dl.read_file(file)

    mask = None
    if with_selection:
        data, mask = dl.feature_selection(data, target)

    time_start, time_stop = None, None

    try:
        app.logger.info("Model in training")
        time_start = time.time()
        algorithms[algorithm_name].train_model(data, target, mask, **options)
        time_stop = time.time()
        app.logger.info("Model trained - elapsed time {}".format(time_stop - time_start))
    except TypeError as e:
        app.logger.error(e)
        abort(status.HTTP_400_BAD_REQUEST, e)

    if mask is not None:
        mask = mask.tolist()

    db.classifier_info.find_one_and_update({'_id': algorithm_name},
                                           {"$set": {"_id": algorithm_name,
                                                     "train_file_size": len(target),
                                                     "options:": options,
                                                     "with_selection": with_selection,
                                                     "training_time": time_stop - time_start}},
                                           upsert=True)

    db.models.find_one_and_update({'_id': algorithm_name},
                                  {"$set": {"pickle": pickle.dumps(algorithms[algorithm_name].model),
                                            "mask":         json_util.dumps(mask)}},
                                  upsert=True)

    return "", status.HTTP_200_OK


def string_match_true(value):
    return value in ['true', 'True', 1]
