def divisor(a, b, c):
    count = 0
    for i in range(a, b):
        if i % c == 0:
            count += 1
    return count
