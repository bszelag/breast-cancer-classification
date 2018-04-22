from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')

client = MongoClient(app.config["DB_URL"],
                     username=app.config["DB_USER"],
                     password=app.config["DB_PASS"],
                     authSource=app.config["DB_NAME"],
                     authMechanism='SCRAM-SHA-1')
db = client[app.config["DB_NAME"]]

from src.backend.dev_module.controller import dev_module
app.register_blueprint(dev_module)
from src.backend.classificators_module.classificators_controller import classificators
app.register_blueprint(classificators)
from src.backend.statistic_module.statistic_controller import statistics
app.register_blueprint(statistics)
