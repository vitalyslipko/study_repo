def mane_function(x, y):
    if x == y:
        return 0
    a = 0
    while a < x and x <= y:
        a += 1
        a = a * 2
    return a
print(mane_function(100, 101))

def test_function(*args):
    for i in args:
        return i + sum(args)