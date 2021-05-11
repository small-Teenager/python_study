"""
list 的特点：有序，索引映射唯一数据，可以重复，任意类型混存，根据需要动态回收内存
"""
from operator import index

a = 10
list1 = [1, 2, 3, 'world']
print(list1, id(list1), type(list1))
print(len(list1))

print(list1[0], id(list1[0]), type(list1[0]))

list2 = list(['hello', 'world', 98, 99, 1, 2])
print(list2, id(list2), type(list2))
# 获取指定位置的索引
print(list2.index('world'))
# start stop step
print(list2[1:5:1])  # ['world', 98, 99, 1]
print(list2[1:5:2])  # ['world', 99]

# loop


# add
print('-------add-------')
print(list1, len(list1))
list1.append(100)
print(list1, len(list1))

print(list1, len(list1))
list1.extend(list2)
print(list1, len(list1))

# delete
print('-------remove-------')
print(list1, len(list1))
list1.remove(1)
print(list1, len(list1))

list1.pop(5)
print(list1, len(list1))
list1.pop()
print(list1, len(list1))

list1.clear()
print(list1, len(list1))

# sort
print('-------sort-------')
list1 = [1, 3, 5, 2, 4]
print(list1, len(list1))
list1.sort()
print(list1, len(list1))
list1.reverse()
print(list1, len(list1))

print(sorted(list1))
print(list1)
