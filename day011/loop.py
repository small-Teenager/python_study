# while

a = 1
while a < 10:
    print(a)
    a += 1

# while

a = 1
while a < 10:
    print(a)
    a += 1
# 1+2+3+...+100
a, sum = 1, 0
while a <= 100:
    sum += a
    a += 1

print('1+2+3+...+100', sum)

# 计算1-100 之间的偶数和
a, sum = 0, 0
while a <= 100:
    sum += a
    a += 2

print('1+...+100之间的偶数和为:', sum)

# for in
for item in 'Python':
    print(item, type(item))

for i in range(10):
    print(i)

for _ in range(5):
    print('人生苦短')

sum = 0
for item in range(0, 101):
    sum += item
print(sum)
