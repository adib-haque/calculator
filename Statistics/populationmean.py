from Calculator.Division import division
from Calculator.Addition import addition


def population_mean(data):
    numbers = len(data)
    total = 0
    for numbers in data:
        total = addition(total, numbers)
    return round(division(numbers, total), 8)
