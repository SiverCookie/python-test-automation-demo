# \\# Python Test Automation Demo

# 

# 

# 

# A small, production-style Python test automation project using:

# 

# \\- Python 3

# 

# \\- Pytest

# 

# \\- Pytest-cov (coverage)

# 

# \\- Structured logging

# 

# \\- GitHub Actions CI/CD

# 

# 

# 

# \\## Project Structure

# 

# 

# 

# src/

# 

# calculator.py

# 

# tests/

# 

# test\\\_calculator.py

# 

# .github/workflows

# 

# python-tests.yml

# 

# \\## Run Tests Locally

# 

# 

# 

# ```bash

# 

# pytest

# 

# 

# 

# Run with Coverage

# 

# 

# 

# pytest --cov=src --cov-report=term-missing

# 

# 

# 

# Generate HTML Test Report

# 

# 

# 

# pytest --html=report.html

# 

# 

# 

# Continuous Integration

# 

# 

# 

# This project includes a GitHub Actions workflow that automatically:

# 

# 

# 

# \&nbsp;   installs dependencies

# 

# 

# 

# \&nbsp;   runs all tests

# 

# 

# 

# \&nbsp;   enforces coverage

# 

# 

# 

# Workflow file: .github/workflows/python-tests.yml

# 

# 

