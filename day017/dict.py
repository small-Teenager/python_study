# dict 无序可变队列
# create
socres = {"name": "张三", "age": 18}
print(socres, type(socres))
person = dict(name='李四', age='20', address='china')
print(person, type(person))

print(dict(), type(dict()))

# get
print('------get-------')

print(socres['name'])
print(socres.get('name'))
print(socres.get('name1'), type(socres.get('name1')))
print(socres.get('name1', 'zhangsan'), type(socres.get('name1')))  # 提供默认值

# exist

print('name' in socres)
print('name' not in socres)

# del
print('-----del-----')
print(socres)
del socres['name']
print(socres)
# add
print('-----add-----')
socres['address'] = 'china'
print(socres)

# keys()
print('-----keys-----')
print(socres)
keys = socres.keys()
print(keys, type(keys))
print(list(keys))

# values()
print('-----values-----')
print(socres)
values = socres.values()
print(values, type(values))
print(list(keys))

# items()
print('-----items-----')
print(socres)
items = socres.items()
print(items, type(items))
print(list(items))

# loop
for items in socres:
    print(items, socres.get(items))
    # print(items, socres[items])
