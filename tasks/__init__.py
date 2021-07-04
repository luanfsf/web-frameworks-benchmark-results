from invoke import Collection

from tasks.dev import Dev
from tasks.help import Help
from tasks.env import Env
from tasks.test import Test
from tasks.template import Template

namespace = Collection(Help, Template, Env, Test, Dev)
