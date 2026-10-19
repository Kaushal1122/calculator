# Calculator CI Runbook

## 1. Overview

This project implements a Python calculator supporting addition, subtraction, and multiplication of two positive integers. It uses pytest for unit testing, Docker for containerization, and GitHub Actions for continuous integration (CI).

## 2. Prerequisites

- Python 3.x
- Git
- Docker Desktop or Docker Engine
- A GitHub account

## 3. Project Structure

```text
calculator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── calculator.py
├── requirements.txt
├── test_calculator.py
└── RUNBOOK.md
```

## 4. Set Up the Project

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/Kaushal1122/calculator.git
cd calculator
```

Create and activate a virtual environment if you want to run tests locally.

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 5. Run Unit Tests Locally

Execute the following command:

```bash
python -m pytest -v
```

Expected result: all 9 tests pass.

## 6. Build and Test the Docker Image

Ensure Docker Desktop or Docker Engine is running.

Build the Docker image:

```bash
docker build -t calculator-app:local .
```

Run the unit tests inside the container:

```bash
docker run --rm calculator-app:local
```

Expected result: all 9 tests pass.

## 7. Continuous Integration

The GitHub Actions workflow is located at `.github/workflows/ci.yml`.

The workflow performs the following steps:

1. Triggers on pushes to `main` and feature branches matching `feature/**`.
2. Triggers on pull requests targeting `main`.
3. Checks out the repository.
4. Builds the Docker image.
5. Runs unit tests inside the Docker container.

### Verify the Workflow

1. Open the calculator repository on GitHub.
2. Navigate to the **Actions** tab.
3. Select the latest **Calculator CI** workflow run.
4. Verify that the Docker build and unit test steps complete successfully.

A successful run should show a green check mark.

## 8. Troubleshooting

### Docker Build Failure

- Ensure Docker Desktop is running.
- Confirm that `Dockerfile` exists in the repository root.
- Review the error output from the Docker build command.

### Unit Test Failure

- Run `python -m pytest -v` locally.
- Review the failed test and check the corresponding calculator implementation.
- Verify that dependencies are installed correctly.

### GitHub Actions Failure

- Open the failed workflow run under the **Actions** tab.
- Inspect the logs for the failed step.
- Reproduce the Docker build and test commands locally to investigate the issue.

## 9. Expected Outcome

The calculator can be tested locally and inside a Docker container. GitHub Actions automatically builds the Docker image and executes the unit tests when the configured GitHub events occur.