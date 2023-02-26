import subprocess
from src.models.deployment import ContractToDeploy


def compile_contract_api(contract: ContractToDeploy):
    wasm_compilation_proc = subprocess.run(["sh", "./utils/compile-to-wasm.sh", contract.lib_file],
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if wasm_compilation_proc.returncode == 0:
        return {"success": True, "message": "Compiled Successfully!"}

    error_message = wasm_compilation_proc.stderr
    return {"success": False, "message": error_message}
