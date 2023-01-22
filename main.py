from typing import Union
from fastapi import FastAPI
from stellar_sdk import Keypair
import requests

app = FastAPI()



def create_account(secret: str = ""):
    raw_account = False
    if secret:
        local_keypair = Keypair.from_secret(secret)
    else:
        raw_account = True
        local_keypair = Keypair.random()
        secret = local_keypair.secret

    pub_key = local_keypair.public_key

    if raw_account:
        successfully_added_fund, message = get_funds_from_friendbot(pub_key)
        if not successfully_added_fund:
            return False, secret, pub_key, message

    if local_keypair.can_sign():
        return True, secret, pub_key, "account successfully created!"
    else:
        return False, secret, pub_key, "invalid secret!"


def get_funds_from_friendbot(public_key: str):
    response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
    if response.status_code == 200:
        return True, "successfully added 10,000 xlms on the testnet!"
    else:
        err_title = response.json()["title"]
        err_message = response.json()["detail"]
        return False, f"error adding funds in testnet due to {err_title}: {err_message}"


@app.get("/")
def read_root():
    return {"status": "running"}


@app.get("/create_account")
def create_account_api():
    acc_created, secret, pub_key, message = create_account()
    return {"bool": acc_created, "secret_seed": secret, "pub_key": pub_key, "message": message}
