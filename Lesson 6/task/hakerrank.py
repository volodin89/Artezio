for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as ze:
        print('Error Code: {}'.format(ze))
    except ValueError as ve:
        print('Error Code: {}'.format(ve))
