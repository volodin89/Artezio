import unittest
from task.task_8 import max_value


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(max_value({1: 1, 2: 4, 3: 9, 4: 16, 5: 25}), [25, 16, 9])

    def test_ok_2(self):
        self.assertEqual(max_value({'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
