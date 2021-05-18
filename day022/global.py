def fun(a, b):
    global c  # 全局变量
    c = a + b
    return c


fun(1, 2)
print(c)
