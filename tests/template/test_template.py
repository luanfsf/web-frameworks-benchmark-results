import unittest

from template.hello_template import hello_template


class TestTemplate(unittest.TestCase):
    def test_hello_template(self):
        self.assertEqual(hello_template(), "Hello Template!")
