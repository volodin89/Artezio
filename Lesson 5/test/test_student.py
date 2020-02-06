import unittest

from task.student import Student

conf = {
    "exam_max": 30,
    "lab_max": 7,
    "lab_num": 10,
    "k": 0.61
}


class MyTestCase(unittest.TestCase):

    def test_ok_1(self):
        a = Student("Alexey", conf)
        for i in range(1, 11):
            a.make_lab(5, i)
        a.make_exam(25)
        self.assertEqual(a.is_certified(), (75, True))

    def test_ok_2(self):
        a = Student("Alexey", conf)
        for i in range(1, 21):
            a.make_lab(5, i)
        a.make_exam(30)
        self.assertEqual(a.is_certified(), (80, True))

    def test_false_1(self):
        a = Student("Alexey", conf)
        for i in range(1, 11):
            a.make_lab(3, i)
        a.make_exam(30)
        self.assertEqual(a.is_certified(), (60, False))

    def test_false_2(self):
        a = Student("Alexey", conf)
        for i in range(1, 21):
            a.make_lab(3, i)
        a.make_exam(25)
        self.assertEqual(a.is_certified(), (55, False))


if __name__ == '__main__':
    unittest.main()
