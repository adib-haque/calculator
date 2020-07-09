from Statistics.populationmean import population_mean
from Calculator.Calculator import sq_rt


def pop_stand_dev(data):
    pop = population_mean(data)
    length = len(data)
    return round(sq_rt(sum([(element - pop) ** 2 for element in data]) / length), 3)
