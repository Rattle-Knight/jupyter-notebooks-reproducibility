import config
import github_access
import notebook_metadata
import conda_setup
import notebook_run
import reporter


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

    ENV_NAME = config.REPO_NAME.replace("/","_")

    conda_setup.create_conda_env(
        env_name = ENV_NAME,
        requirements_path = config.DIR + "/requirements.txt",
        conda_path = config.CONDA_DIR
        )

    notebook_run.access_notebook(
        config.DIR,
        ENV_NAME,
        config.CONDA_DIR,
        )

    reporter.generate_full_notebook_report(
        config.DIR
        )

   
    
