def mane_function(x, y):
    if x == y:
        return 0
    a = 0
    while a < x and x <= y:
        a += 1
        a = a * 2
    return a