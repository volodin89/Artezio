class Observable:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        kwargs = (', '.join(f"{key}={repr(val)}" for (key, val)
                            in self.__dict__.items() if not key.startswith('_')))
        return f"{self.__class__.__name__}({kwargs})"
