try:
    a, b = 100, 1
    c = a / b
except:
    ZeroDivisionError:\
        print('division by zero', c, a, b)

print('over')


try:
    a, b = 100, 0
    c = a / b
except:
    ZeroDivisionError: \
        print('division by zero', c, a, b)
else:
    print('c',c)

print('over')