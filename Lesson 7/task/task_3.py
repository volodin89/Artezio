from functools import partial


def carry(func):
    argc = func.__code__.co_argcount
    if argc == 0:
        return func

    def wrapper(*args):
        if len(args) >= argc:
            return func(*args)
        else:
            return partial(wrapper, *args)

    return wrapper
