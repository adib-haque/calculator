def pop_stand_dev(data):
    u = population_mean(data)
    leng = len(data)
    return round(square_root(sum([(element - u) ** 2 for element in data]) / leng), 3)