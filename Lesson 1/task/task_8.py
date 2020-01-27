def max_value(dct):
    num = []
    lst = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 3):
        num.append(lst[i][1])
    return num
