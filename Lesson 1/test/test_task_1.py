import unittest
from task.task_1 import capital_letter


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(capital_letter("alison heck"), "Alison Heck")

    def test_ok_2(self):
        self.assertEqual(capital_letter("12abc"), "12abc")

    def test_exception(self):
        self.assertRaises(ValueError, capital_letter, "")


if __name__ == '__main__':
    unittest.main()
