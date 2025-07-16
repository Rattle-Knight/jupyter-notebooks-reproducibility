# notebook_reporter.py
import nbformat
import json
from pathlib import Path

def generate_notebook_report(notebook_dir, report_output_path="notebook_report.json"):

    notebook_dir = Path(notebook_dir)
    for path in notebook_dir.rglob("*.ipynb"):
        notebook_path = path

    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    error_cells = []

    print("[5] generating report")

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
        "status": "success" if not error_cells else "failure",
        "error_count": len(error_cells),
        "error_cells": error_cells
    }

    with open(report_output_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(f" Notebook report written to: {report_output_path}")