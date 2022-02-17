import os
import os.path


def find_python_files(root):
    ''' Recursively search a directory indicated by `root` for a list
    of python source files. '''
    return [
        os.path.join(r, file) for r, _, f in os.walk(root) for file in f
        if file.endswith(".py")
    ]
