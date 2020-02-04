from functools import reduce


def mul_and_sum(*args, **kwargs):
    lst = []
    total_lst = []
    for values in args:
        lst.append(values)
    for value in kwargs.values():
        lst.append(value)

    def flatten(lst):
        for item in lst:
            if isinstance(item, (list, tuple)):
                if item == lst:
                    return False
                if not flatten(item):
                    return False
            else:
                total_lst.append(item)
        return True

    if flatten(lst):
        total_sum = reduce(lambda x, y: x + y, total_lst)
        total_mul = reduce(lambda x, y: x * y, filter(lambda i: i != 0, total_lst))
        return total_sum, total_mul
    print("Cyclic reference was found!")
    return None
