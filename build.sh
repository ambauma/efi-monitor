#!/usr/bin/env bash
set -e

setup_venv() {
    rm -rf venv/
    python_executable="python3"
    if ! command -v python3 &> /dev/null
    then
    echo "WARNING: python3 is not found.  Assuming python exists!"
    fi
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip wheel setuptools
    pip install --editable .[TEST]
}

test() {
    pydocstyle efi_monitor tests/
    pylint efi_monitor/ tests/
    pytest --cov=efi_monitor tests/
}

build() {
    pip install --upgrade twine build
    python -m build
    python -m twine upload --repository pypi dist/*
}

"$@"
