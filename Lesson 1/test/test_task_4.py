import unittest
from task.task_4 import counter


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        self.assertEqual(counter(['abc', 'xyz', 'aba', '1221']), 2)

    def test_ok_2(self):
        self.assertEqual(counter(['vnvwkn', 'ljanvkl', 's', '12214', '155481', '846848878']), 3)


if __name__ == '__main__':
    unittest.main()
