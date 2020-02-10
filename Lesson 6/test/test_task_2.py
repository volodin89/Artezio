import unittest
from task.task_2 import generator_attr


class MyTestCase(unittest.TestCase):

    def test_1(self):
        string = "Hello, world!"
        self.assertEqual(generator_attr(string), ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
                                                  'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
                                                  'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                                                  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
                                                  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
                                                  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
                                                  'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
                                                  'title', 'translate', 'upper', 'zfill'])


if __name__ == '__main__':
    unittest.main()
