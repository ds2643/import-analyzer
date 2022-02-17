import os

import pytest

import analysis


TEST_REPOSITORY = "dev-resources/test-repository"


def test_get_imports_by_example():
    python_file = os.path.join(TEST_REPOSITORY, "a.py")
    imports = [imp for imp in analysis.get_imports(python_file)]
    assert "os" in imports[0][1], "Module name discovery may not work."
    assert "Tensorflow" in imports[1][0], "Module parent discovery may not work."
    assert imports[1][2] is None, "Aliasing improperly bound."


def test_get_imports_count():
    python_file = os.path.join(TEST_REPOSITORY, "a.py")
    imports = [imp for imp in analysis.get_imports(python_file)]
    assert len(imports) == 3, "Import count is wrong"


def test_no_imports():
    python_file = os.path.join(TEST_REPOSITORY, "c.py")
    imports = [imp for imp in analysis.get_imports(python_file)]
    assert not imports, "Python module with no imports should not produce imports"


def test_import_variants():
    python_file = os.path.join(TEST_REPOSITORY, "b.py")
    imports = [imp for imp in analysis.get_imports(python_file)]

    import_from = imports[0]
    parents = import_from[0]
    module_name = import_from[1][0]
    assert len(parents) == 3 and module_name == "taste"

    aliased_import = imports[1] 
    alias = aliased_import[2]
    assert "Tensorflow" in aliased_import[1] and not aliased_import[0]
    assert alias == "tf", "Description of aliasing fails"
