import unittest
from task.task_6 import dict_generator


class MyTestCase(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(dict_generator(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})


if __name__ == '__main__':
    unittest.main()
