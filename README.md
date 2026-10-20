# Python App with GitHub Actions (CI/CD)

Welcome to the **app_github_actions** project! This repository serves as a simple guide and hands-on setup for understanding version control, automated testing, and CI/CD workflows using GitHub Actions and `uv`.

---

## 1. Key Concepts & Definitions

Here are quick, plain-English definitions for the core concepts used in this project:

* **Git**: A local tool on your computer that acts like a time-machine for your code. It records changes you make so you can roll back to previous versions if anything breaks.
* **GitHub**: A cloud website that hosts your Git repositories. It allows multiple developers to collaborate, share code, and propose changes through Pull Requests (PRs).
* **CI/CD (Continuous Integration / Continuous Deployment)**:
  * **Continuous Integration (CI)**: Automatically building and running tests on every new code update to ensure no bugs or broken features are introduced.
  * **Continuous Deployment (CD)**: Automatically releasing and deploying tested code to servers or cloud environments so users can access the updates immediately.
* **GitHub Actions**: A built-in service on GitHub that automates your development pipeline (CI/CD). It runs automated tasks (like testing Python code) inside cloud machines every time code is pushed.
* **Workflow**: A customizable automated process configured using a `.yml` file stored inside `.github/workflows/`. It defines *when* (triggers like a push or PR) and *what* (steps like installing dependencies and running tests) GitHub should execute.

---

## 2. Developer Workflow

Here is how code moves through a standard development pipeline:

1. **Feature Development**: Create a new branch locally and make code edits in your IDE (e.g., VS Code).
2. **Push & Pull Request (PR)**: Push your local branch to GitHub and create a Pull Request targeting the `main` branch.
3. **Automated CI Checks**: Opening a PR automatically triggers the GitHub Actions workflow, which builds the environment and runs unit tests.
4. **Code Review & Merge**: Team members review the code. Once checks pass and review is approved, the branch is merged into `main`.

---

## 3. Local Environment Setup

We use **`uv`** by Astral as our fast Python package manager.

### Prerequisites
* Python 3.10+
* Terminal / PowerShell

### Installation & Initialization

1. Install `uv` on your machine:
   * **Windows (PowerShell):**
     ```powershell
     irm https://astral.sh/uv/install.ps1 | iex
     ```
   * **macOS / Linux:**
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

2. Clone this repository and sync dependencies:
   ```bash
   git clone https://github.com/Latrechesara/app_github_actions.git
   cd app_github_actions
   uv sync
   ```

3. Run local unit tests manually:
   ```bash
   uv run pytest
   ```

---

## 4. GitHub Actions Workflow Configuration

The automated pipeline is defined inside `.github/workflows/main.yml`:

```yaml
name: CI Python Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version-file: ".python-version"

    - name: Install uv
      uses: astral-sh/setup-uv@v5
      with:
        enable-cache: true

    - name: Install dependencies
      run: uv sync --frozen

    - name: Run tests with pytest
      run: uv run pytest
```
