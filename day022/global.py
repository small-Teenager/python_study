def fun(a, b):
    global c
    c = a + b
    return c


fun(1, 2)
print(c)
