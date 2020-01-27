def dict_generator(n):
    dct = {x: x * x for x in range(1, n + 1)}
    return dct


print(dict_generator(5))
