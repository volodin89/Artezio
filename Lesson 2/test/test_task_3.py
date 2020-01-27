import unittest
from task.task_3 import factorial


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(factorial(1), 1)

    def test_ok_2(self):
        self.assertEqual(factorial(5), 120)

    def test_ok_(self):
        self.assertEqual(factorial(0), None)


if __name__ == '__main__':
    unittest.main()
