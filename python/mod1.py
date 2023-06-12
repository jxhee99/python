def normal_sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(1) == type(a) and type(1) == type(b):
        ret = normal_sum(a, b)
    else:
        return

    return ret