from time import sleep, time


def time_it(func):
    def wrapper(*args, **kwargs):
        current_time = time()
        result = func(*args, **kwargs)
        print(f'Average working time: {int(time() - current_time) * 1000} ms')
        return result

    return wrapper


def time_methods(*methods):
    def inner_decorator(class_instance):
        def wrapper(*args, **kwargs):
            for method in methods:
                if hasattr(class_instance, method):
                    setattr(class_instance, method, time_it(getattr(class_instance, method)))
            return class_instance(*args, **kwargs)

        return wrapper

    return inner_decorator


@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


a = Spam(2)
a.inspect()
a.foo()
