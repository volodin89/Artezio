import unittest
from task.task_7 import merge_dict


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(
            merge_dict({'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}),
            {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_ok_2(self):
        self.assertEqual(merge_dict({1: 1, 2: 2, 3: 3}, {4: 4, 2: 5, 6: 6}), {1: 1, 2: 5, 3: 3, 4: 4, 6: 6})


if __name__ == '__main__':
    unittest.main()
