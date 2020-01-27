def subsets(set_1, set_2, set_3):
    if set_3 & set_1 and set_3 & set_2:
        return True
    return False
