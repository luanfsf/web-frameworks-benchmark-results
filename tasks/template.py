from invoke import task, Collection, call

from tasks.defaults import DOT_ENV
from tasks.env import load

env_pre_tasks = [
    call(load, path=DOT_ENV),
]


@task(pre=env_pre_tasks, default=True)
def hello_template(c):
    """Run template"""
    c.run(f"python template/hello_template.py")


Template = Collection("template", hello_template)
