import subprocess
import os
import sys


def command(command_list):
    try:
        subprocess.run(command_list, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)

def create_conda_env(env_name, requirements_path,conda_path):
    if not os.path.isfile(requirements_path):
        print(f"Error: {requirements_path} not found.")
        sys.exit(1)
    
    #creation of the env
    command([conda_path, "create", "--yes", "--name", env_name, "python"])

    #installing the packages
    command([conda_path, "run", "--name", env_name, "pip", "install", "-r", requirements_path])




