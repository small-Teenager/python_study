# 集合 无重复元素
# create
print('--------crete----------')
set1 = {1, 4, 2, 3, 1}
print(set1, type(set1), id(set1))

set2 = set(range(6))
print(set2, type(set2), id(set2))

set3 = set({'hello', 'world', 'python'})
print(set3, type(set3), id(set3))

set4 = set({})
print(set4, type(set4), id(set4))

# add update
print('--------add update----------')
set5 = set({10, 20, 30})
set5.add(40)
print(set5, type(set5), id(set5))
set5.update([50, 60, 70])
set5.update((80, 90, 100))
print(set5, type(set5), id(set5))
# remove discard pop
print('--------remove discard pop----------')
set5.remove(40)  # 删除不存在元素会抛异常
print(set5, type(set5), id(set5))
set5.discard(500)  # 删除不存在元素不会抛异常
print(set5, type(set5), id(set5))

set5.pop()
print(set5, type(set5), id(set5))

set5.clear()
print(set5, type(set5), id(set5))

# == !=
set6 = {1, 2, 3}
set7 = {1, 2, 3}

print(set6 == set7, id(set6), id(set7))
print(set6 != set7, id(set6), id(set7))
# 是否子集
set8 = {2, 3}
print(set8.issubset(set7))
# 是否超集
print(set7.issuperset(set8))
print(set7.issuperset(set7))
# 是否有交集  有交集False 无交集True
print(set7.isdisjoint(set8))












