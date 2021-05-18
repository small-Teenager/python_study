# 递归
# 斐波那契数列 第n位
def fib(n):
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))


# 斐波那契数列

def flibsOne(numMax):
    c = []
    a, b = 0, 1
    while a < numMax:
        a, b = b, a + b
        c.append(a)
    c.remove(c[-1])
    print(c)


flibsOne(11)


# 阶乘
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
