import subprocess


#config and Access vars
ACCESS_TOKEN = None  
REPO_NAME = "hughshanahan/CS2900-Lab-1"
BRANCH = "master"
DIR = "./git_repo_downloads"
CONDA_DIR = r""


def command(command_list):
    try:
        return subprocess.run(command_list, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)
