import pandas as pd


def get_module_references(imports):
    assert isinstance(imports, dict)
    
    module_references = [
        ".".join(mod + name) for mod, name, _ in
        sum(imports.values(), [])
    ]

    module_references = pd.DataFrame(module_references, columns=["module"])
    return module_references.module.value_counts()


