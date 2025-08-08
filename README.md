
# Reproducibility of Juypter Noebooks

This project provides a framework for verifying the reproducibility of Jupyter Notebooks. It automates the process of downloading, executing, and analyzing notebooks, ensuring that their results can be consistently reproduced.

## Overview
The tool performs the following steps:

- Downloads a specified notebook from GitHub using its unique identifier.
- Performs multiple checks and generates a metadata JSON file describing the notebook.
- Creates a dedicated Conda environment using the dependencies listed in the requirements.txt file.
- Runs the notebook in the prepared environment.
- Logs cell execution failures and error details.
- Saves error report as a JSON file in the Outputs directory for further analysis.
 
## Requirements
- Python3
- Anaconda 
- PyGithub
- nbformat

## Config
To run this tool, you will need to set up the **config.py** file.

Add your Github personal access token here:
```
ACCESS_TOKEN = "YOUR GITHUB ACCESS TOKEN"
```
Add your Github repository and branch here:
```
REPO_NAME = "REPO YOU WOULD LIKE TO ASSESS"
BRANCH = "BRANCH NAME ON GITHUB"
```


Add the path to your "\condabin\conda.bat" file here:
```
CONDA_DIR = "YOUR CONDA.BAT INSTALLATION PATH"
```

## Usage
To run this tool, you must run 	**main.py** after congfiguring **config.py** (directions provided above).

The tool will run in the terminal, output 6 key stages of the pipeline.

<img width="1763" height="788" alt="Program Pipeline" src="https://github.com/user-attachments/assets/f0e10abd-7877-446d-927c-445c50115d24" />

## Output
A report will be generated as a json file within the Outputs folder.
This will detail cells that failed after the trial Notebook run was completed.


