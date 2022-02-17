from invoke import task
import subprocess as sp


@task
def run(context, organization, repository):
    '''Run repository analysis.'''
    cmd = f"pipenv run python -m main {organization} {repository}"
    sp.run(cmd, shell=True)


@task
def test(context):
    '''Run repository tests.'''
    cmd = "pipenv run python -m pytest -v"
    sp.run(cmd, shell=True)
