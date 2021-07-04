from invoke import task, Collection, call

from tasks.env import load
from tasks.defaults import TEST_DOT_ENV

env_pre_tasks = [
    call(load, path=TEST_DOT_ENV),
]


@task(
    pre=env_pre_tasks,
    default=True,
    help={"module": "Test module path e.g. (path.to.test.module) "},
)
def test(c, module=""):
    """Run all tests or the one specified  in module <module>. Uses .env.test as env"""
    c.run(f"python -m unittest {module} ")


@task(pre=env_pre_tasks)
def coverage(c):
    """Run tests with coverage"""
    c.run("coverage run --source='.' -m unittest")


@task(pre=env_pre_tasks)
def coverage_report(c):
    """Shows coverage report"""
    c.run("coverage report")


@task(pre=env_pre_tasks)
def coverage_html(c):
    """Creates coverage html report"""
    c.run("coverage html")


Test = Collection("test", test, coverage, coverage_report, coverage_html)
