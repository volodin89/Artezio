import unittest
from task.task_4 import cycle


class MyTestCase(unittest.TestCase):

    def test_1(self):
        arr = [1, 2, 3]
        a = cycle(arr)
        for i in range(0, 3):
            next(a)
        self.assertEqual(next(a), 1)

    def test_2(self):
        arr = [1, 2, 3]
        a = cycle(arr)
        for i in range(0, 4):
            next(a)
        self.assertEqual(next(a), 2)

    def test_3(self):
        arr = [1, 2, 3]
        a = cycle(arr)
        for i in range(0, 5):
            next(a)
        self.assertEqual(next(a), 3)


if __name__ == '__main__':
    unittest.main()
