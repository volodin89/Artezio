import io
import unittest.mock
from task.complex import Complex


class MyTestCase(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_add(self, mock_stdout):
        C = Complex([2, 1])
        D = Complex([5, 6])
        print(C + D)
        self.assertEqual(mock_stdout.getvalue(), "7.00+7.00i\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_sub(self, mock_stdout):
        C = Complex([2, 1])
        D = Complex([5, 6])
        print(C - D)
        self.assertEqual(mock_stdout.getvalue(), "-3.00-5.00i\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_mul(self, mock_stdout):
        C = Complex([2, 1])
        D = Complex([5, 6])
        print(C * D)
        self.assertEqual(mock_stdout.getvalue(), "4.00+17.00i\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_truediv(self, mock_stdout):
        C = Complex([2, 1])
        D = Complex([5, 6])
        print(C / D)
        self.assertEqual(mock_stdout.getvalue(), "0.26-0.11i\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_abs_a(self, mock_stdout):
        C = Complex([2, 1])
        print(abs(C))
        self.assertEqual(mock_stdout.getvalue(), "2.24+0.00i\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_abs_b(self, mock_stdout):
        D = Complex([5, 6])
        print(abs(D))
        self.assertEqual(mock_stdout.getvalue(), "7.81+0.00i\n")


if __name__ == '__main__':
    unittest.main()
