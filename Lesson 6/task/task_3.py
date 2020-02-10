def made_dict(lst_1, lst_2):
    total_lst = dict(zip(lst_1, lst_2 + [None] * (len(lst_1) - len(lst_2))))
    return total_lst
