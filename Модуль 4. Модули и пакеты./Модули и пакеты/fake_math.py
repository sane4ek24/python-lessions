from math import inf


def fake_divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second
