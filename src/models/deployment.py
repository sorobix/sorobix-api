from pydantic import BaseModel


class ContractToDeploy(BaseModel):
    lib_file: str
    secret_key: str
