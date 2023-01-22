from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from stellar_sdk import Keypair
import requests
import subprocess


class ContractToDeploy(BaseModel):
    lib_file: str
    secret_key: str

class ContractToInvoke(BaseModel):
    contract_id: str
    contract_function: str
    secret_key: str
    contract_arguments: list[str]

class Contract(BaseModel):
    lib_file: str


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
    response = requests.get(
        f"https://friendbot-futurenet.stellar.org?addr={public_key}")

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
    return {"success": acc_created, "secret_seed": secret, "pub_key": pub_key, "message": message}


@app.post("/deploy_contract")
def deploy_to_chain_api(contract: ContractToDeploy):

    if len(contract.secret_key) == 0:
        acc_created, secret, pub_key, message = create_account()
        if not acc_created:
            return {"success": False, "contract_id": None, "message": "Please create an account manually via /create_account and try again!"}

        secret_key = secret
    else:
        secret_key = contract.secret_key

    deploy_contract_proc = subprocess.run(["sh", "./utils/deploy-contract.sh", contract.lib_file, secret_key],
                                          stdout=subprocess.PIPE, universal_newlines=True)

    contract_id = deploy_contract_proc.stdout

    if contract_id != '':
        return {"success": True, "contract_id": contract_id, "message": "Succesfully deployed contract!", "secret_seed": secret, "pub_key": pub_key}

    return {"success": False, "contract_id": None, "message": "Something went wrong!"}


@app.post("/compile_contract")
def compile_contract_api(contract: ContractToDeploy):
    wasm_compilation_proc = subprocess.run(["sh", "./utils/compile-to-wasm.sh", contract.lib_file],
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if wasm_compilation_proc.returncode == 0:
        return {"success": True, "message": "Compiled Successfully!"}

    error_message = wasm_compilation_proc.stderr
    return {"success": False, "message": error_message}
    
@app.post("/invoke_contract")
def invoke_contract_api(contract: ContractToInvoke):
    base_call = f"soroban invoke \
    --id {contract.contract_id} \
    --secret-key {contract.secret_key} \
    --rpc-url http://localhost:8000/soroban/rpc \
    --network-passphrase 'Test SDF Future Network ; October 2022' \
    --fn {contract.contract_function} \
    "
    for arg in contract.contract_arguments:
        base_call += f"--arg {arg} "
    invoke_contract_proc = subprocess.run([base_call],shell=True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if invoke_contract_proc.stdout != '':
        return {"success": True, "results": invoke_contract_proc.stdout}
    else:
        return {"success": False, "results": invoke_contract_proc.stderr}

