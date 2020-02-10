import unittest
from task.task_1 import EvenIterator


class MyTestCase(unittest.TestCase):

    def test_1(self):
        a = EvenIterator([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(next(a), 2)

    def test_2(self):
        a = EvenIterator([1, 2, 3, 4, 5, 6, 7])
        next(a)
        self.assertEqual(next(a), 4)

    def test_3(self):
        a = EvenIterator([1, 2, 3, 4, 5, 6, 7])
        next(a)
        next(a)
        self.assertEqual(next(a), 6)

    def test_4(self):
        a = EvenIterator([1, 2, 3, 4, 5, 6, 7])
        next(a)
        next(a)
        next(a)
        self.assertRaises(StopIteration, next, a)


if __name__ == '__main__':
    unittest.main()
