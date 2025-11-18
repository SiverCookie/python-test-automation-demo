# 🧪 Python Test Automation Demo  
**A small but complete Python testing project using Pytest, logging, and GitHub Actions CI.**

This project demonstrates a clean and practical example of Python test automation using modern best practices. It includes:

- Clean project layout (`src/` + `tests/`)
- Unit tests using **Pytest**
- Code coverage support
- Centralized logging
- GitHub Actions CI pipeline that runs tests automatically
- Requirements file & reproducible environment

---

## 📁 Project Structure

python-test-automation-demo/
│
├── src/
│ ├── calculator.py # Core module under test
│ └── init.py # Logging setup
│
├── tests/
│ ├── test_calculator.py # Test suite
│ └── init.py
│
├── requirements.txt # Dependencies
├── README.md
└── .github/workflows/
└── python-tests.yml # GitHub CI pipeline


---

## 🚀 Getting Started

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt

2️⃣ Run all tests

pytest

3️⃣ Run tests with coverage report

pytest --cov=src --cov-report=term-missing

🧰 Features
✔ Automated Unit Testing

Unit tests cover all functions from calculator.py using Pytest.
✔ Logging

Logging is configured in src/__init__.py.
A logs/app.log file is automatically created the first time the module is imported.

Example log entry:

2025-01-01 12:00:00 - calculator - INFO - Adding numbers 2 and 3

✔ GitHub Actions CI

Every push triggers:

    repository checkout

    Python setup

    dependency install

    test execution

Workflow file: .github/workflows/python-tests.yml
CI status appears in the Actions tab on GitHub.
📌 Example Code
Source: src/calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

Tests: tests/test_calculator.py

from src.calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

🧾 Requirements

pytest
pytest-cov

🎯 Purpose of the Project

This repository demonstrates:

    Python scripting fundamentals

    Unit testing and assertions

    Test automation workflows

    Good folder structure

    CI/CD basics using GitHub Actions

    Logging and maintainability

Useful for:

    QA/Test Automation Engineer portfolios

    DevOps learning paths

    Technical interview preparation

📬 Author

Vlad Opriș
Python Automation • Embedded • DevOps Learner
GitHub: https://github.com/SiverCookie
