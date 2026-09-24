name: Automated Integration Check

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

permissions:
  contents: read

jobs:
  run-test-suite:
    runs-on: ubuntu-latest

    steps:
      - name: Fetch Code base
        uses: actions/checkout@v4

      - name: Initialize Python Runtime
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Bind System Dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Execute Pytest Automation Suite
        run: python -m pytest
