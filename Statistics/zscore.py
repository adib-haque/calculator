from Statistics.populationmean import population_mean
from Statistics.populationstandarddeviation import pop_stand_dev
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def z_score(numbers):
    row_value = 151
    std_dev = pop_stand_dev(numbers)
    mean = population_mean(numbers)
    result = subtraction(row_value, mean)
    z_score_ = division(result, std_dev)
    print(z_score_)
    return z_score_
