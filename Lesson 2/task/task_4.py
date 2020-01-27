def my_range(start=0, stop=None, step=1):
    if start == 0 and stop == None:
        raise Exception("Put a limit")

    if stop == None:
        stop = start
        start = 0

    lst = []
    value = start
    i = 0

    if step > 0:
        while value < stop - step:
            value = start + step * i
            lst.append(value)
            i += 1

    if step < 0:
        while value > stop - step:
            value = start + step * i
            lst.append(value)
            i += 1

    return lst
