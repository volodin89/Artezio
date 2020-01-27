def capital_letter(str):
    if len(str) > 0 and len(str) < 1000:
        return (" ").join(w.capitalize() for w in str.split(" "))
    else:
        raise ValueError
