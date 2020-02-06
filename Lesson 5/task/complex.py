from math import sqrt


class Complex:

    def __init__(self, lst):
        self.real = float(lst[0])
        self.imag = float(lst[1])

    def __add__(self, other):
        _r = self.real + other.real
        _i = self.imag + other.imag
        return Complex([_r, _i])

    def __sub__(self, other):
        _r = self.real - other.real
        _i = self.imag - other.imag
        return Complex([_r, _i])

    def __mul__(self, other):
        _r = self.real * other.real - self.imag * other.imag
        _i = self.real * other.imag + self.imag * other.real
        return Complex([_r, _i])

    def __truediv__(self, other):
        _r = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
        _i = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
        return Complex([_r, _i])

    def __abs__(self):
        _r = sqrt(self.real ** 2 + self.imag ** 2)
        return Complex([_r, 0])

    def __repr__(self):
        if self.imag >= 0:
            return "{:.2f}+{:.2f}i".format(self.real, self.imag)
        return "{:.2f}{:.2f}i".format(self.real, self.imag)


if __name__ == "__main__":
    C = Complex(input().split())
    D = Complex(input().split())
    print(C + D)
    print(C - D)
    print(C * D)
    print(C / D)
    print(abs(C))
    print(abs(D))
