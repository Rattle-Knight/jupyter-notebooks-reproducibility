import config
import github_access
import notebook_metadata


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
