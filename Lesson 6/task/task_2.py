def generator_attr(obj):
    attr = [i for i in dir(obj) if not i.startswith("_")]
    return attr
