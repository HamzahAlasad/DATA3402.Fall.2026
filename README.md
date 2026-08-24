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
2. Until Lab 3, browse materials here on GitHub and download the files you need
   (the fork/clone setup comes later — see *Labs and submission* below).
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

Lab work is submitted through your own **fork** of this repository:

- you fork this repository once on GitHub, giving you your own copy under your account;
- you **pull from this repository** to receive new lectures and labs as they are released;
- you do your lab work in your fork and **push to your fork**, which is where it is graded.

**Do not fork or clone anything yet.** We set this up together, step by step, in the
lab session that covers git and GitHub (Lab 3) — doing it early or differently will
leave you with a setup that fights the course workflow all semester. Until then, you
only need the environment from *Getting started* below; lecture materials can be
browsed right here on GitHub. `Labs/DATA3402_Lab3_Merge_Conflict_Guide.pdf` covers
what to do when git fights you.

## Communication

All course communication goes through Teams — not email.
