def z_score(num):
    z_mean = populationmean(num)
    sd = stddev(num)
    zlist = []
    for x in num:
        z = round(division(subtraction(x, z_mean), sd), 6)
        zlist.append(z)
    return zlist