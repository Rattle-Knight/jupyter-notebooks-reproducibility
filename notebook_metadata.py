import nbformat
import json
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

    if not directory_path.is_dir():
        print(f"The path {directory} is not a directory.")
        return

    for path in directory_path.rglob("*.ipynb"):
        metadata = extract_notebook_metadata(path)
        if metadata:
            print(f"\nMetadata for: {path}")
            print(json.dumps(metadata, indent=2))
