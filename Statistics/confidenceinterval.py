from Statistics.populationmean import population_mean
from Statistics.populationstandarddeviation import pop_stand_dev
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.SquareRoot import sq_rt


def confidence_interval(data):
    z_value = 1.960
    mean = population_mean(data)
    sd = pop_stand_dev(data)

    x = len(data)
    y = division(sq_rt(x), sd)

    margin_of_error = multiplication(z_value, y)

    a = [subtraction(mean, margin_of_error)]
    b = [addition(mean, margin_of_error)]

    size = len(a)
    lower = a[0]
    upper = b[0]

    return lower, upper
