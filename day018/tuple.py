# 可变序列：字典，列表
# 不可变序列：字符串 元组
# 为什么元组设计为不可变？多任务环境下，同时操作对象不需要加锁

lst = [10, 20, 30]
print(id(lst))
lst.append(58)
print(id(lst))

str = 'hello'
print(id(str))
str += 'world'
print(id(str))

# create
print('-------create-------')
t = ('python', 'java', 'c++')
print(t, type(t), id(t))
t2 = tuple(('python', 'java', 'c++', 'c'))
print(t2, type(t2), id(t2))

t3 = ('python', 'java', 'c++')
print(t3, type(t3), id(t3))
t3 = ('python', 'java', 'c++', 'c')
print(t3, type(t3), id(t3))

# 空列表 空字典 空元组
lst1 = []
lst2 = list()
d1 = {}
d2 = dict()
t1 = ()
t2 = tuple()
print('空列表', lst1, lst2, type(lst1), type(lst2))
print('空字典', d1, d2, type(d1), type(d2))
print('空元组', t1, t2, type(t1), type(t2))
# index
t = (10, [20, 30], 40)
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
#t[0]=40
#print(t[0], type(t[0]), id(t[0]))
t[1].append(10)
print(t[1], type(t[1]), id(t[1]))
# loop
print('--------loop-------')
t = (10, [20, 30], 40)
for item in t:
    print(item)






