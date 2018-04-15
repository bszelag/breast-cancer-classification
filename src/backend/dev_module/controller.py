from flask import Blueprint

dev_module = Blueprint('dev_module', __name__, url_prefix='/dev')


@dev_module.route('/status')
def backend_status():
    return "Backend is running"
