from src.backend import app
from flask import Blueprint, request, abort, jsonify
from flask_api import status
import src.data_preparation.data_loader as dl
import src.data_visualization.data_printer as dp
import src.classificators.naive_bayes as nb
import src.classificators.svm as svm
import src.classificators.decision_tree as tree


classificators = Blueprint('classificators', __name__)
training_in_progress = False

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
    return_dict = {"accuracy": dp.get_classification_accuracy(predicted, target),
                   "predicted_values": dp.match_ids_with_predicted_values(ids, predicted)}
    return jsonify(return_dict)


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
