import unittest
from task.task_5 import chain


class MyTestCase(unittest.TestCase):

    def test_1(self):
        lst_1 = [1, 2, 3]
        lst_2 = [4, 5, 6]
        lst_3 = [6, 7, 8]
        a = chain(lst_1, lst_2, lst_3)
        next(a)
        self.assertEqual(next(a), 2)

    def test_2(self):
        lst_1 = [1, 2, 3]
        lst_2 = [4, 5, 6]
        lst_3 = [6, 7, 8]
        a = chain(lst_1, lst_2, lst_3)
        for i in range(0, 4):
            next(a)
        self.assertEqual(next(a), 5)

    def test_3(self):
        lst_1 = [1, 2, 3]
        lst_2 = [4, 5, 6]
        lst_3 = [6, 7, 8]
        a = chain(lst_1, lst_2, lst_3)
        for i in range(0, 7):
            next(a)
        self.assertEqual(next(a), 7)


if __name__ == '__main__':
    unittest.main()
