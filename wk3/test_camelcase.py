import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):
     def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelcase.camel_case('HelloWorld'))
        self.assertEqual('', camelcase.camel_case(''))
        