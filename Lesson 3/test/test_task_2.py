import unittest
from task.task_2 import mul_and_sum

ARR = [15, 16, 17]
ARR.append(ARR)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(mul_and_sum(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])),
                         (75, 1596672000))

    def test_2(self):
        self.assertEqual(mul_and_sum(1, 2, ARR, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])), None)


if __name__ == '__main__':
    unittest.main()
