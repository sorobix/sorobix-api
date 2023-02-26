from pydantic import BaseModel


class ContractToInvoke(BaseModel):
    contract_id: str
    contract_function: str
    secret_key: str
    contract_arguments: list[str]
