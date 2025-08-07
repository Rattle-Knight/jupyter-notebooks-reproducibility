import subprocess
import sys
import reporter


#config and Access variables
ACCESS_TOKEN = None  
REPO_NAME = "hughshanahan/CS2900-Lab-4"
BRANCH = "master"
DIR = "./git_repo_downloads"
CONDA_DIR = r"C:\Users\JCARe\anaconda3\condabin\conda.bat"
OUTPUT_DIR = "./outputs"


#keeps track of stage of assessment
stage = ""

#wrapper function for usage of subprocesses, if it fails will report errors.
def command(command_list, **kwargs):
    try:
        return subprocess.run(command_list, check=True, **kwargs)
    except subprocess.CalledProcessError as e:
        print("Error Handling Command:",e)
        reporter.report_errors(e)
        sys.exit(1)
