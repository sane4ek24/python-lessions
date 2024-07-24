from math import inf
def divide(first, second):
    if second == 0:
        print(inf)
    return first / second

s = divide(1,0)
print(s)