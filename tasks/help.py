from invoke import task
import subprocess


@task(default=True, name="help")
def Help(c):
    """Get info on tasks usage"""
    print(
        "Invoking tasks:\n\n  invoke <task> [arg] to run a task\n  invoke --help <task> to get info on a task\n"
    )
    subprocess.run("invoke --list", shell=True)
