from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.SquareRoot import sq_rt
from Calculator.Square import square
from Statistics.sampledata import get_sample
from Statistics.populationmean import population_mean
import random


def sample_std_dev(data):
    total = 0
    samples = random.randint(1, len(data))
    new_samples = get_sample(data, samples)
    new_mean = population_mean(new_samples)
    for number in new_samples:
        result = subtraction(number, new_mean)
        sq = square(result)
        total = addition(total, sq)
    n = len(new_samples)
    d = division(subtraction(1, n), total)
    sample_sd = sq_rt(d)
    return sample_sd
