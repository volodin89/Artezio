import io
import unittest.mock
from task.observable import Observable


class X(Observable):
    pass


class MyTestCase(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ok(self, mock_stdout):
        x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
        print(x)
        self.assertEqual(mock_stdout.getvalue(), "X(foo=1, bar=5, name='Amok', props=('One', 'two'))\n")


if __name__ == '__main__':
    unittest.main()
