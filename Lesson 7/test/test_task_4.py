import io
import unittest.mock
from task.task_4 import check_type_args, AnnotationError


class MyTestCase(unittest.TestCase):
    def test_ok_1(self):
        @check_type_args
        def foo(a: int, b: int):
            return a + b

        self.assertEqual(foo(4, 5), None)

    def test_ok_2(self):
        @check_type_args
        def foo(a: int, b: int, c: int = 3):
            return a + b + c

        self.assertEqual(foo(4, 5, c=4), None)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_annotation_1(self, mock_stdout):
        @check_type_args
        def foo(a: int, b: str):
            return a + b

        foo(4, 5)
        self.assertEqual(mock_stdout.getvalue(), "Incorrect argument type\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_annotation_2(self, mock_stdout):
        @check_type_args
        def foo(a: int, b: int, c: str = 3):
            return a + b + c

        foo(4, 5, c=4)
        self.assertEqual(mock_stdout.getvalue(), "Incorrect argument type\n")

    def test_exc_1(self):
        @check_type_args
        def foo(a: int, b):
            return a + b

        self.assertRaises(AnnotationError, foo, 4, 5)

    def test_exc_2(self):
        @check_type_args
        def foo(a: int, b: int, c=3):
            return a + b + c

        self.assertRaises(AnnotationError, foo, 4, 5, c=4)


if __name__ == '__main__':
    unittest.main()
