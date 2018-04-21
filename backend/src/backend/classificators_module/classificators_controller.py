from pymongo.collection import Collection

from src.backend import app, db
from flask import Blueprint, request, abort, jsonify
from flask_api import status
import src.data_preparation.data_loader as dl
import src.data_visualization.data_printer as dp
import src.classificators.naive_bayes as nb
import src.classificators.svm as svm
import src.classificators.decision_tree as tree
import bson.json_util as json_util
import datetime


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
        abort(status.HTTP_404_NOT_FOUND)

    if "with_target" not in request.form:
        app.logger.error('Missing target info')
        abort(status.HTTP_400_BAD_REQUEST)

    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST)

    if algorithms[algorithm_name].model is None:
        app.logger.info("Model not trained yet")
        abort(status.HTTP_406_NOT_ACCEPTABLE)

    if request.form['with_target'] in ['true', 'True', 1]:
        with_target = True
    else:
        with_target = False

    file = request.files['file'].read().decode('ascii')
    file = file.splitlines()

    data, target, ids = dl.read_file(file, with_target)
    predicted = algorithms[algorithm_name].model.predict(data)
    accuracy = dp.get_classification_accuracy(predicted, target, inPercent=False)
    total = len(predicted)

    return_dict = {"accuracy": {k: v*100/total for k, v in accuracy.items()},
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
    return_dict["time"] = datetime.datetime.utcnow()
    collection.insert_one(return_dict)

    return json_util.dumps(return_dict)


@classificators.route('/<algorithm_name>/train', methods=['POST'])
def train_model(algorithm_name):

    if algorithm_name not in algorithms:
        app.logger.error("Wrong algorithm name in url")
        abort(status.HTTP_404_NOT_FOUND)

    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST)

    file = request.files['file'].read().decode('ascii')
    file = file.splitlines()

    data, target, ids = dl.read_file(file)
    algorithms[algorithm_name].train_model(data, target)
    return "", status.HTTP_200_OK


@classificators.route('/<algorithm_name>/stats', methods=['GET'])
def get_stats(algorithm_name):
    return "TODO"
