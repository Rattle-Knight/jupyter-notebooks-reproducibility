# notebook_reporter.py
import nbformat
import json
import config
from pathlib import Path
import os

def report_errors(error):

    error_info = {
        "Stage Failure": str(config.stage),
        "type": type(error).__name__,
        "message": str(error)
    }


    with open(os.path.join(config.OUTPUT_DIR, "notebook_report.json"), "w", encoding="utf-8") as f:
        json.dump(error_info, f, indent=2)

    print(f" Notebook report written to: {report_output_path}")

def generate_full_notebook_report(notebook_dir):

    notebook_dir = Path(notebook_dir)
    notebook_name = None

    for path in notebook_dir.rglob("*.ipynb"):
        notebook_path = path
        notebook_name = path.name

    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    error_cells = []


    config.stage = "[6] Generating Report"
    print(config.stage)

    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == "code" and "outputs" in cell:
            for output in cell.outputs:
                if output.output_type == "error":
                    error_cells.append({
                        "cell_index": idx,
                        "ename": output.get("ename"),
                        "evalue": output.get("evalue"),
                        "traceback": output.get("traceback")
                    })

    output_json = {
        "notebook_name": notebook_name,
        "status": "success" if not error_cells else "failure",
        "error_count": len(error_cells),
        "error_cells": error_cells
    }

    with open(os.path.join(config.OUTPUT_DIR, "notebook_report.json"), "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)


    outputpath = os.path.join(config.OUTPUT_DIR, "notebook_report.json")
    print(f" Notebook report written to: {outputpath}")