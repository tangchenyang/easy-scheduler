from unittest import TestCase

from confparser.json_parser import JsonParser


class TestJsonParser(TestCase):

    def test_parse(self):
        parser = JsonParser()
        print(parser.parse('{ "task_name": "task1", "task_type": "bash" }'))
        self.assertEqual(parser.parse('{ "task_name": "task1", "task_type": "bash" }'), {"key": "value"})
