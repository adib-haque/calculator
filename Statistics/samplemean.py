from Calculator.Division import division


def sample_mean(data):
    data_samples = data[0:999]
    num = len(data_samples)
    return round(division(num, sum(data_samples)), 1)
