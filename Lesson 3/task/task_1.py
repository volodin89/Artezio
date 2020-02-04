def one(lst):
    sqr = [i * i for i in lst]
    return sqr


def two(lst):
    even_numbers = [lst[i] for i in range(0, len(lst), 2)]
    return even_numbers


def three(lst):
    cube = [lst[i] ** 3 for i in range(1, len(lst), 2) if lst[i] % 2 == 0]
    return cube
