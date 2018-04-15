from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from src.backend.dev_module.controller import dev_module
app.register_blueprint(dev_module)
from src.backend.classificators_controlers.bayes_controller import bayes
app.register_blueprint(bayes)
