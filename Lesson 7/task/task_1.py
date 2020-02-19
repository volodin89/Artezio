from time import sleep, time
from functools import reduce


def average_time(n=1):
    def inner_decorator(function):
        times = []

        def wrapper(*args, **kwargs):
            current_time = time()
            result = function(*args, **kwargs)
            times.append((time() - current_time) * 1000)
            total_time = reduce(lambda x, y: x + y, times[-n:])
            if len(times) == 1:
                print(f'Average working time: {int(times[0])} ms')
            elif 1 < len(times) < n:
                print(f'Average working time: {int(total_time / len(times))} ms')
            else:
                print(f'Average working time: {int(total_time / n)} ms')
            return result

        return wrapper

    return inner_decorator


@average_time(n=2)
def foo(a):
    sleep(a)
    return a
