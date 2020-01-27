def counter(arr):
    count = 0
    for str in arr:
        if len(str) > 1 and str[0] == str[-1]:
            count += 1
    return count
