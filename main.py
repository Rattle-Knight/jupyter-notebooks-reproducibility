import config
import github_access
import notebook_metadata
import conda_setup


if __name__ == "__main__":
    github_access.download_github_files(
        repo_name=config.REPO_NAME,
        branch=config.BRANCH,
        local_dir=config.DIR,
        token=config.ACCESS_TOKEN  
    )
    notebook_metadata.process_notebooks(
        config.DIR
        ) 
    conda_setup.create_conda_env(
        env_name = config.REPO_NAME.replace("/","_"),
        requirements_path = config.DIR + "/requirements.txt",
        conda_path = config.CONDA_DIR
        )

    ## 3 include system specs
    ## 2 running full notebook 
    ### report on cells that fail
    
