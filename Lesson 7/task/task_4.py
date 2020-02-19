class AnnotationError(Exception):
    pass


def check_type_args(func):
    annotation = func.__annotations__

    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) != len(annotation):
            raise AnnotationError("Not all arguments are annotated")
        d_kwargs = dict(zip(annotation.keys(), args))
        for (k, v) in annotation.items():
            if k in d_kwargs:
                if not isinstance(d_kwargs[k], v):
                    print("Incorrect argument type")
            if k in kwargs:
                if not isinstance(kwargs[k], v):
                    print("Incorrect argument type")

    return wrapper
