import sys
import os
import tempfile

import analysis
import git_utils
import reporting
import util


TARGET_MODULE = "tensorflow"


# TODO: Accept both local and hosted repositories.
def main(organization, repository, target_module):

    with tempfile.TemporaryDirectory() as temp_dir:
        repository_path = git_utils.pull(temp_dir, organization, repository)

        assert os.path.exists(repository_path), \
            f"{repository_path} doesn't exist."

        tf_imports = dict()
        for python_file in util.find_python_files(repository_path):
            imps = [
                imp for imp in analysis.get_imports(python_file)
                if target_module in imp[0] or target_module == imp[1]
            ]
            if imps:
                tf_imports[python_file] = imps

        summary = reporting.get_module_references(tf_imports)
        return summary.to_string()


if __name__ == "__main__":
    organization = sys.argv[1]
    repository = sys.argv[2]
    assert organization and repository, (
        "Specify target GitHub organization/repository."
    )
    result = main(organization, repository, TARGET_MODULE)
    print(result)
