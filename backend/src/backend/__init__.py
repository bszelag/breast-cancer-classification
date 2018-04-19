from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from src.backend.dev_module.controller import dev_module
app.register_blueprint(dev_module)
from src.backend.classificators_module.classificators_controller import classificators
app.register_blueprint(classificators)
