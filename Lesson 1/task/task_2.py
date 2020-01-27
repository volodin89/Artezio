def counter(str):
    dct = {}
    for elem in str:
        dct[elem] = str.count(elem)
    return dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))
