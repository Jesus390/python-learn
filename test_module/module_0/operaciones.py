def suma(*args):
    total = 0
    for i in args:
        if isinstance(i, (list, tuple)):
            total += sum(i)
            continue
        total += i
    return total

def resta(*args):
    total = 0
    for i in args:
        if isinstance(i, (list, tuple)):
            total -= sum(i)
            continue
        total -= i
    return total

if __name__=="__main__":
    print(suma((10, 22, -12), 1, [1, -32, 2, 2], 3, 2, 3, 3))
    print(resta((10, -22, -12), 1, [1, 32, -2, 2], 3, 2, 3, 3))