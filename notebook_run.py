import subprocess
import nbformat
from config import command
from pathlib import Path



def access_notebook(notebookdir,env_name,conda_path):
    notedir = Path(notebookdir)
    for path in notedir.rglob("*.ipynb"):
        notebook_path = path

    print("[4] running notebook")
    result = subprocess.run([
        conda_path, "run", "-n", env_name,
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", "--inplace",
        "--ExecutePreprocessor.allow_errors=True",
        notebook_path
    ], capture_output=True, text=True)

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)


 
