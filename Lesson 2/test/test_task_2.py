import unittest
from task.task_2 import divisor


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(divisor(15, 30, 3), 5)

    def test_ok_2(self):
        self.assertEqual(divisor(15, 31, 3), 6)


if __name__ == '__main__':
    unittest.main()
