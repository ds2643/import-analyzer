import os

import pytest

import analysis
import reporting

target_module = "Tensorflow"
test_python_file = os.path.join(
    "dev-resources", "test-repository", "a.py"
)
test_imports = [
    imp for imp in analysis.get_imports(test_python_file) 
    if target_module in imp[0] or target_module == imp[1]
]


def test_get_module_references():
    summary = reporting.get_module_references({"a.py" : test_imports})
    assert len(summary) == 2, "Expected two imports"


