import unittest
from task.task_9 import cleaner


class MyTestCase(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(cleaner([1, 1, 2, 2, 3, 3, 4, 4, 1, 2, 3, 4]), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
