from ..models.invoke import ContractToInvoke
from ..utils.soroban_client import prepare_soroban, call_soroban


def invoke_contract_api(contract: ContractToInvoke):
    statement = prepare_soroban("invoke", contract)
    return call_soroban(statement)
