from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication


def var_pop_proportion(data):
    p = proportion(data)
    q = subtraction(1, p)
    n = len(data)
    return division(n, multiplication(p, q))