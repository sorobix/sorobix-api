import subprocess
from src.models.invoke import ContractToInvoke


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
    invoke_contract_proc = subprocess.run(
        [base_call], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if invoke_contract_proc.stdout != '':
        return {"success": True, "results": invoke_contract_proc.stdout}
    else:
        return {"success": False, "results": invoke_contract_proc.stderr}
