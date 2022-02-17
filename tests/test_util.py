import os

import pytest   

import util


def test_file_discovery():
    test_repository_path = os.path.join("dev-resources", "test-repository")
    files = util.find_python_files(test_repository_path)

    assert files, "python files not found."
    assert len([f for f in files if f.endswith(".py")]) == len(files), (
        "Non python files included."
    )
    assert all([os.path.exists(f) for f in files]), "Some files don't exist."
