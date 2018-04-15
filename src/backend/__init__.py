from flask import Flask
from src.backend.dev_module.controller import dev_module

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(dev_module)
