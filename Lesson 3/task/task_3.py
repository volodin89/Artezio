def foo(a, b, c, d, max_arg=[]):
    lst = [a, b, c, d]

    def max_attr():
        return max(lst)

    if not max_arg or max_arg[0] < max_attr():
        max_arg.insert(0, max_attr())
    average_attr = sum(lst) / len(lst)
    return average_attr, max_arg[0]
