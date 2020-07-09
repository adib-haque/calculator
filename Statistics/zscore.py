from coverage import data
from Statistics.populationmean import population_mean
from Statistics.populationstandarddeviation import pop_stand_dev
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def z_score(num):
    z_mean = population_mean(data)
    new_data = [float(x) for x in data]
    nd = new_data[1]

    pop_std = pop_stand_dev(new_data)
    y = subtraction(nd, z_mean)
    z = division(pop_std, y)
    return z
