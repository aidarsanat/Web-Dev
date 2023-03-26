def xor(x, y):
    ok = False
    if (x == 1 and y == 0) or (x == 0 and y == 1):
        print(1)
        ok = True
    if ok == False:
        print(0)


a, b = map(int, input().split())
xor(a, b)