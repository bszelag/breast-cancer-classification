from flask import Blueprint, request, abort, jsonify
from src.backend import app, db
import bson.json_util as json_util
from flask_api import status

statistics = Blueprint("statistics", __name__, url_prefix='/stats')


@statistics.route("/<algorithm_name>")
def get_options(algorithm_name):
    return json_util.dumps(db.classifier_options.find_one({'_id': algorithm_name}))


@statistics.route("/<algorithm_name>/history/<number>", methods=["GET"])
def get_history(algorithm_name, number):
    collection = db.get_collection(algorithm_name + "_history")
    try:
        num = int(number)
    except ValueError:
        abort(status.HTTP_400_BAD_REQUEST, "last field in url needs to be an integer")

    return json_util.dumps(collection.find().limit(num).sort("$natural", -1))


@statistics.route("/<algorithm_name>/total_accuracy", methods=["GET"])
def get_total_accuracy(algorithm_name):
    return json_util.dumps(db.total_accuracy.find({"_id": algorithm_name}))


@statistics.route("/<algorithm_name>/total_accuracy/reset", methods=["GET"])
def reset_total_accuracy(algorithm_name):
    db.total_accuracy.find_one_and_update({"_id": algorithm_name}, {"$set": {"total": 0,
                                                                             "tp": 0,
                                                                             "tn": 0,
                                                                             "fp": 0,
                                                                             "fn": 0}})
    return "", status.HTTP_200_OK
