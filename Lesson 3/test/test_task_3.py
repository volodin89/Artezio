import unittest
from task.task_3 import foo


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(foo(1, 2, 3, 4), (2.5, 4))

    def test_2(self):
        self.assertEqual(foo(-3, -2, 10, 1), (1.5, 10))

    def test_3(self):
        self.assertEqual(foo(7, 8, 8, 1), (6.0, 10))


if __name__ == '__main__':
    unittest.main()
