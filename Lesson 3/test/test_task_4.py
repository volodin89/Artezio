import unittest
from task.task_4 import build_tree


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(build_tree('<root><element1 /><element2 /><element3><element4 /></element3></root>'),
                         (({
                               'name': 'root',
                               'children': [
                                   {'name': 'element1', 'children': []},
                                   {'name': 'element2', 'children': []},
                                   {
                                       'name': 'element3',
                                       'children': [
                                           {'name': 'element4', 'children': []}
                                       ]
                                   }
                               ]
                           }, 2)))


if __name__ == '__main__':
    unittest.main()
