
# Reproducibility of Juypter Noebooks

A tool for testing the Reproducibility of a Juypter Notebook


## Description
This tool will:
 - first download a given notebook off of Github given its identifier, 
 - then it will perform several checks to produce a metadata json file
 - it will then take the Requirments.txt file that has the dependancies of the notebook, setting up a conda env with it
 - then it will run the notebook, collecting errors on cells which fail.
 - finally a report will be recorded into a json file within an Output Folder
 
## Requirements
- Python3
- Anaconda 
- PyGithub
- nbformat

## Config
To run this tool you will need to setup the config.py file as such
add your Github personal access token here
```
ACCESS_TOKEN = "YOUR GITHUB ACCESS TOKEN"
```
Add your Github repository and branch here
```
REPO_NAME = "REPO YOU WOULD LIKE TO ASSESS"
BRANCH = "BRANCH NAME ON GITHUB"
```


Add the path to your "\condabin\conda.bat" file here
```
CONDA_DIR = "YOUR CONDA.BAT INSTALLATION PATH"
```

## Usage
this tool will run in the terminal and will output 6 key stages of the pipeline.

<img width="1763" height="788" alt="Program Pipeline" src="https://github.com/user-attachments/assets/f0e10abd-7877-446d-927c-445c50115d24" />



