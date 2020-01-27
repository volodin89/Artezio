import unittest
from task.task_5 import subsets


class MyTestCase(unittest.TestCase):

    def test_true(self):
        self.assertTrue(subsets(set([1, 2]), set([2, 3]), set([2])))

    def test_false(self):
        self.assertFalse(subsets(set([1, 2]), set([3, 4]), set([5])))


if __name__ == '__main__':
    unittest.main()
