import os
from pprint import pprint
from invoke import task, Collection
from dotenv import load_dotenv, dotenv_values

from tasks.defaults import DOT_ENV, PROTECTED_KEYS


@task(default=True)
def check(c):
    """Check if .env is present in current working directory"""
    dot_env = ".env"
    exists = "a" if os.path.exists(dot_env) else "no"
    print(f"There is {exists} {dot_env} file at {os.getcwd()}/!")


@task(help={"path": "Path to .env file path, default is (tasks.defaults.DOT_ENV)"})
def load(c, path=DOT_ENV):
    """Loads .env file variables"""
    load_dotenv(dotenv_path=path)


@task(name="list")
def _list(c):
    """list environment variables"""
    pprint(os.environ, indent=4)


@task(help={"path": ".env file path."})
def view(c, path=DOT_ENV):
    """View .env file variables, except the ones declared in (tasks.default.PROTECTED_KEYS)"""
    dot_env = dotenv_values(dotenv_path=path)
    for key in PROTECTED_KEYS:
        if dot_env.get(key):
            dot_env[key] = f"[__HIDDEN__]{dot_env.get(key)[-5:]}"
    pprint(dot_env, indent=4)


Env = Collection("env", check, load, _list, view)
