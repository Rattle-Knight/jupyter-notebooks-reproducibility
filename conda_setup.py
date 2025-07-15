import os
import sys
from config import command



def create_conda_env(env_name, requirements_path,conda_path):
    if not os.path.isfile(requirements_path):
        print(f"Error: {requirements_path} not found.")
        sys.exit(1)
    
    print("[2] creating enviroment")
    #creation of the env
    command([conda_path, "create", "--yes", "--name", env_name, "python", "jupyter", "ipykernel"])

    print("[3] installing packages")
    #installing the packages
    command([conda_path, "run", "--name", env_name, "pip", "install", "-r", requirements_path])




