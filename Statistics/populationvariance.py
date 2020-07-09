from Statistics.populationmean import population_mean
from Calculator.Division import division


def population_variance(data):
    pop = population_mean(data)
    length = len(data)
    return round(division(length, sum([(element - pop) ** 2 for element in data])), 3)
