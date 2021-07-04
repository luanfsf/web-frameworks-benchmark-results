from invoke import task, Collection, call
import subprocess

from tasks.defaults import DOT_ENV
from tasks.env import load

env_pre_tasks = [
    call(load, path=DOT_ENV),
]


@task(help={"path": "Folder or file to apply black"})
def black(c, path="."):
    """Make it all black or make <path> black"""
    subprocess.run(f"black {path}", shell=True)


Dev = Collection("dev", black)
