import os
import urllib.request
from github import Github
import config

def download_github_files(repo_name, branch="main", local_dir="./", token=None):

    config.stage = "[0] accessing github"
    print(config.stage)

    if token:
        git = Github(token)
    else:
        git = Github()  #unauthenticated (60 req/hr limit)

    repo = git.get_repo(repo_name)
    contents = repo.get_contents("", ref=branch)



    download_recursive(contents, repo, branch, local_dir)

    config.stage = "[1] downloaded files"
    print(config.stage)


def download_recursive(contents_list, repo, branch, local_dir):

    for content_file in contents_list:

        ##directory recusion
        if content_file.type == "dir":
            
            new_contents = repo.get_contents(content_file.path, ref=branch)
            download_recursive(new_contents, repo, branch, local_dir)
    
        ##file download
        elif content_file.type == "file":
            save_path = os.path.join(local_dir, content_file.path)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            try:
                urllib.request.urlretrieve(content_file.download_url, save_path)

            except Exception as e:
                continue



    
