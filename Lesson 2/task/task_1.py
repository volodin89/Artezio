def sqr(n):
    count = 0
    for i in range(1, n + 1, 2):
        count += 1
        print("Sqr {0} = {1}. Count of numbers = {2}".format(i, i ** 2, count))


sqr(5)
sqr(6)
sqr(7)
sqr(8)
