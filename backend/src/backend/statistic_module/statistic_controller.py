from src.backend import app, db
from flask import Blueprint, request, abort, jsonify

statistics = Blueprint("statistic", __name__, url_prefix='/stats')


@statistics.route("/<algorithm_name>/history", method=["GET"])
def get_history(algorithm_name):
    return "TODO"


@statistics.route("/<algorithm_name>/total_accuracy", method=["GET"])
def get_total_accuracy(algorithm_name):
    return "TODO"


@statistics.route("/<algorithm_name>/total_accuracy/reset", method=["GET"])
def get_total_accuracy(algorithm_name):
    return "TODO"
