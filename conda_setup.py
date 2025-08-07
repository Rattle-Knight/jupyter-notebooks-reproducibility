import os
import sys
import config
import json



def create_conda_env(env_name, requirements_path,conda_path):
    if not os.path.isfile(requirements_path):
        print(f"Error: {requirements_path} not found.")
        sys.exit(1)

    with open(os.path.join(config.OUTPUT_DIR, "metadata.json"), "r", encoding="utf-8") as f:
        metadata = json.load(f)

    kernelspec = metadata.get("kernelspec", {})
    language_info = metadata.get("language_info", {})
    
    python_version = language_info.get("version")
    print("kspec",kernelspec)
    print("linfo",language_info)
    print("python",python_version)


    config.stage = "[3] creating enviroment"
    print(config.stage)
    config.command([conda_path, "create", "--yes", "--name", env_name, str("python="+python_version), "jupyter", "ipykernel"])

    config.stage = "[4] installing packages"
    print(config.stage)
    config.command([conda_path,"activate", env_name], shell=True) #env warmup for first runs
    config.command([conda_path, "run", "--name", env_name, "pip", "install", "-r", requirements_path])




