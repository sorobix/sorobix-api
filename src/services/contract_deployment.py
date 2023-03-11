import subprocess
from src.models.deployment import ContractToDeploy
from src.services.account_creation import create_account


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
