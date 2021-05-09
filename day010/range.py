# range 的三种创建方式

# range(stop)
r = range(10)
print(r)  # range(0, 10)
print(type(r))
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(start,stop)
r = range(3, 10)
print(r)  # range(3, 10)
print(type(r))
print(list(r))  # [3, 4, 5, 6, 7, 8, 9]

# range(start,stop,step)
r = range(3, 10, 3)
print(r)  # range(3, 10, 3)
print(type(r))
print(list(r))  # [3, 6, 9]
print(4 in r)
print(4 not in r)
print(6 not in r)
print(6 in r)
