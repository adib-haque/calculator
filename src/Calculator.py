import math


def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(a) - float(b)


def multiplication(a, b):
    return float(a) * float(b)


def division(a, b):
    if int(b) is not 0:
        return float(a) / float(b)
    else:
        return 'Error, Divisor b cannot be 0'


def square(a):
    a = int(a)
    return math.pow(a, 2)


def srt(a):
    a = float(a)
    return math.sqrt(a)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a, b):
        self.result = srt(a)
        return self.result
