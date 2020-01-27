import unittest
from task.task_4 import my_range


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(my_range(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_ok_2(self):
        self.assertEqual(my_range(0, 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_ok_3(self):
        self.assertEqual(my_range(0, 10, 2), [0, 2, 4, 6, 8])

    def test_ok_4(self):
        self.assertEqual(my_range(10, 0, -1), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_ok_5(self):
        self.assertEqual(my_range(10, -6, -2), [10, 8, 6, 4, 2, 0, -2, -4])


if __name__ == '__main__':
    unittest.main()
