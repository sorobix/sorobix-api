from stellar_sdk import Keypair
import requests


def create_account(secret: str = None):
    raw_account = False
    if secret:
        keypair = Keypair.from_secret(secret)
    else:
        raw_account = True
        keypair = Keypair.random()
        secret = keypair.secret

    pub_key = keypair.public_key

    if raw_account:
        successfully_added_fund, message = get_funds_from_friendbot(pub_key)
        if not successfully_added_fund:
            return False, secret, pub_key, message

    if keypair.can_sign():
        return True, secret, pub_key, "Account successfully created!"
    else:
        return False, secret, pub_key, "Invalid Secret!"


def get_funds_from_friendbot(public_key: str):
    response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
    if response.status_code == 200:
        return True, "Successfully added 10,000 XLMs on the TestNet!"
    else:
        err_title = response.json()["title"]
        err_message = response.json()["detail"]
        return False, f"Error adding funds in Testnet due to {err_title}: {err_message}"


def main():
    acc_created, secret, pub_key, message = create_account()

    print("Success Bool: ", acc_created)
    print("Secret Seed: ", secret)
    print("Pub Key: ", pub_key)
    print("Message: ", message)


main()
