import nbformat
import json
import config
import os
from pathlib import Path

def extract_notebook_metadata(notebook_path):
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
            return notebook.metadata
    except Exception as e:
        print(f"Error reading {notebook_path} - {e}")
    return None


def process_notebooks(directory="."):
    directory_path = Path(directory)

    config.stage = "[2] accessing kernel info"
    print(config.stage)

    if not directory_path.is_dir():
        print(f"The path {directory} is not a directory.")
        return

    for path in directory_path.rglob("*.ipynb"):
        metadata = extract_notebook_metadata(path)

        if metadata is not None:
            # Extract only the relevant keys for env creation
            filtered_metadata = {
                "kernelspec": metadata.get("kernelspec", {}),
                "language_info": metadata.get("language_info", {})
            }

            with open(os.path.join(config.OUTPUT_DIR, "metadata.json"), 'w', encoding='utf-8') as outfile:
                json.dump(filtered_metadata, outfile, indent=2)

 

