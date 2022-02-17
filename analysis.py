import ast
from collections import namedtuple


Import = namedtuple("Import", ["module", "name", "alias"])


# NOTE: Approach attributed to StackOverflow user "GaretJax".
# NOTE: Assumes all imports are unique.
def get_imports(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path)

    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue

        for n in node.names:
            yield Import(module, n.name.split('.'), n.asname)
