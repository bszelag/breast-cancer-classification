from src.backend import app
from flask import Blueprint, request, abort, jsonify
from flask_api import status
import src.data_preparation.data_loader as dl
import src.classificators.naive_bayes as nb
import src.data_visualization.data_printer as dp

bayes = Blueprint('bayes', __name__, url_prefix='/bayes')
model = None
training_in_progress = False


# TODO: make it work without target info in send file
@bayes.route('/predict', methods=['POST'])
def get_classification():
    global model

    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST)

    if model is None:
        app.logger.info("Model not trained yet")
        abort(status.HTTP_204_NO_CONTENT)

    data, target, ids = dl.read_file(request.files['file'])
    predicted = model.predict(data)
    return jsonify(dp.get_classification_accuracy(predicted, target))


@bayes.route('/train', methods=['POST'])
def train_model():
    if not request.files:
        app.logger.error('Missing file')
        abort(status.HTTP_400_BAD_REQUEST)

    global model
    data, target, ids = dl.read_file(request.files['file'])
    model = nb.get_trained_model(data, target)
    return "", status.HTTP_200_OK


@bayes.route('/stats', methods=['GET'])
def get_stats():
    return "TODO"
