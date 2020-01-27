def get_difference(list1, list2):
    new_list = list(set(list1) ^ set(list2))
    return new_list


print(get_difference(["Саша", "Маша", "Вася", "Петя", "Гриша"], ["Маша", "Петя", "Ира"]))
