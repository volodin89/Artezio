import unittest
from task.task_3 import string_cutter


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(string_cutter("w3resource"), "w3ce")

    def test_ok_2(self):
        self.assertEqual(string_cutter("w3"), "w3w3")

    def test_ok_3(self):
        self.assertEqual(string_cutter("w"), "")


if __name__ == '__main__':
    unittest.main()
