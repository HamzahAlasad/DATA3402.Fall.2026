# DATA 3402 — Python for Data Science 2

**Fall 2026 · University of Texas at Arlington · Instructor: Amir Farbin**

Course materials are distributed through this repository. Pull regularly — lectures
and labs are pushed as the semester progresses.

## Contents

| Path | What's there |
|------|--------------|
| `syllabus.pdf` | Course syllabus, grading breakdown, policies |
| `Lectures/` | One folder per lecture: notebooks and/or slide PDFs |
| `Labs/` | One folder per lab assignment, plus setup guides |
| `sample.ipynb` | Minimal notebook to check your environment works |
| `requirements.txt` | Python packages used in the course |

## Getting started

1. Read `Labs/Git Hub Setup Guide (wsl & Mac Os).pdf` and get git working on your machine.
2. Clone this repository.
3. Set up a Python environment and install the requirements:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Launch Jupyter and open `sample.ipynb` to confirm everything runs:

   ```bash
   jupyter lab
   ```

You need Linux, macOS, or Windows with WSL. Google Colab is an acceptable fallback
if your machine can't handle the later assignments.

## Notes on large data

Several lectures and labs use datasets too large to keep in git (the SUSY dataset,
Kaggle competition data, image sets). Those are downloaded by the notebooks
themselves and are excluded via `.gitignore` — don't commit them.

## Labs and submission

Lab assignments are distributed and collected through GitHub Classroom. Accept the
assignment link posted on Teams, work in the repository it creates for you, and push
your work before the deadline. `Labs/DATA3402_Lab3_Merge_Conflict_Guide.pdf` covers
what to do when git fights you.

## Communication

All course communication goes through Teams — not email.
