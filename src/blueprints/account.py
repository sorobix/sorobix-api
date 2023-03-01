from src.services.account_creation import create_account_api

from flask import Blueprint

account_blueprint = Blueprint(name="account_blueprint", import_name=__name__)


@account_blueprint.route('/', methods=['GET'])
def read_root():
    return {"status": "running"}


@account_blueprint.route('/generate', methods=['GET'])
def create_account_blueprint():
    return create_account_api()
