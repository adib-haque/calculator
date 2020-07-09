from Statistics.samplemean import sample_mean
from Statistics.Proportion import proportion
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication


def var_sample_proportion(data):
    sample_data = data[0:999]
    sample_prop_data = []
    for x in sample_data:
        if x > 64:
            sample_prop_data.append(x)
    sample_len = len(sample_prop_data)
    sample_len_data = len(sample_data)
    p = round(sample_len / sample_len_data, 6)
    q = subtraction(1, p)
    return round(multiplication(p, q) / (sample_len_data - 1), 6)
