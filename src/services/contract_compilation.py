import subprocess
from pathlib import Path


def compile_contract_api(lib_file: str):
    curr_dir = Path(__file__).parent
    src_path = str(Path(curr_dir).parents[0])

    wasm_compilation_proc = subprocess.run(["sh", src_path + "/utils/compile-to-wasm.sh", lib_file],
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if wasm_compilation_proc.returncode == 0:
        return {"success": True, "message": "Compiled Successfully!"}

    error_message = wasm_compilation_proc.stderr

    return {"success": False, "message": str(error_message)}
