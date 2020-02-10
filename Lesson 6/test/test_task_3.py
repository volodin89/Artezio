import unittest
from task.task_3 import made_dict


class MyTestCase(unittest.TestCase):

    def test_1(self):
        lst_1 = ["one", "two", "three", "four", "five"]
        lst_2 = [1, 2, 3, 4, 5]
        self.assertEqual(made_dict(lst_1, lst_2), {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5})

    def test_2(self):
        lst_1 = ["one", "two", "three", "four", "five"]
        lst_2 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(made_dict(lst_1, lst_2), {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5})

    def test_3(self):
        lst_1 = ["one", "two", "three", "four", "five", "six", "seven"]
        lst_2 = [1, 2, 3, 4, 5]
        self.assertEqual(made_dict(lst_1, lst_2), {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': None,
                                                   "seven": None})


if __name__ == '__main__':
    unittest.main()
