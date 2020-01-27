def factorial(num):
    while num > 0:
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)
