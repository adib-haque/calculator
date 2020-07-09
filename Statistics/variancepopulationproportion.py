def var_pop_proportion(data):
    p = proportion(data)
    q = subtraction(1, p)
    n = len(data)
    return division(n, multiplication(p, q))