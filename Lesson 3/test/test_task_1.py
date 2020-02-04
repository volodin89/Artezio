import unittest
from task.task_1 import one, two, three


class MyTestCase(unittest.TestCase):

    def test_one_1(self):
        self.assertEqual(one([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_two_1(self):
        self.assertEqual(two([1, 2, 4, 40, 5, 7, 9, 8, 6, 13, 37, 4]), [1, 4, 5, 9, 6, 37])

    def test_two_2(self):
        self.assertEqual(two([2, 7, 8, 13, 15, 42, 38, 55, 56, 37, 10]), [2, 8, 15, 38, 56, 10])

    def test_three_1(self):
        self.assertEqual(three([1, 2, 4, 4, 5, 7, 9, 8, 6, 13, 37, 4]), [8, 64, 512, 64])

    def test_three_2(self):
        self.assertEqual(three([2, 7, 8, 14, 15, 4, 38, 5, 6, 6, 10]), [2744, 64, 216])


if __name__ == '__main__':
    unittest.main()
