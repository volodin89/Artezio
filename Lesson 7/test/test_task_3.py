import unittest
from task.task_3 import carry


class MyTestCase(unittest.TestCase):
    def test_1(self):
        @carry
        def foo(a, b):
            return a + b

        self.assertEqual(foo(1)(5), 6)

    def test_2(self):
        @carry
        def foo(a, b, c):
            return a + b + c

        self.assertEqual(foo(1)(5)(3), 9)

    def test_3(self):
        @carry
        def foo(a, b, c, d):
            return a + b + c + d

        self.assertEqual(foo(1)(2)(3)(4), 10)


if __name__ == '__main__':
    unittest.main()
