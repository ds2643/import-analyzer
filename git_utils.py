import os
from urllib.parse import urljoin

from git import Repo


def pull(temp_dir, organization, repository):
    repository_path = os.path.join(temp_dir, repository)
    parts = "/".join([organization, f"{repository}.git"])
    git_url = urljoin("https://github.com/", parts)
    Repo.clone_from(git_url, repository_path) 
    return repository_path
