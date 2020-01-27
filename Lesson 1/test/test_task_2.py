import unittest
from task.task_2 import counter


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(counter("google.com"), {'o': 3, 'm': 1, 'l': 1, 'g': 2, 'e': 1, 'c': 1, '.': 1})

    def test_2(self):
        self.assertEqual(counter("paranavigar"), {'a': 4, 'r': 2, 'p': 1, 'n': 1, 'v': 1, 'i': 1, 'g': 1})

    def test_3(self):
        self.assertEqual(counter("we are the champions"), {'e': 3, ' ': 3, 'a': 2, 'h': 2,
                                                           'w': 1, 'r': 1, 't': 1, 'c': 1, 'm': 1, 'p': 1,
                                                           'i': 1, 'o': 1, 'n': 1, 's': 1})


if __name__ == '__main__':
    unittest.main()
