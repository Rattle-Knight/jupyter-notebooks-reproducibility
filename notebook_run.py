import subprocess
import nbformat
import config 
from pathlib import Path


def access_notebook(notebookdir,env_name,conda_path):
    notedir = Path(notebookdir)
    for path in notedir.rglob("*.ipynb"):
        notebook_path = path

    config.stage = "[5] Running Notebook"
    print(config.stage)

    # this runs the notebook before the reporting
    result = config.command([
        conda_path, "run", "-n", env_name,
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute", "--inplace",
        "--ExecutePreprocessor.allow_errors=True",
        notebook_path
    ], capture_output=True, text=True)





 
