from flask import Flask
from .blueprints.contract import contract_blueprint
from .blueprints.account import account_blueprint

app = Flask(__name__)
app.register_blueprint(account_blueprint, url_prefix="/account")
app.register_blueprint(contract_blueprint, url_prefix="/contract")

if __name__ == "__main__":
    app.run()
