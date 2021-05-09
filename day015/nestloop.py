# 嵌套循环
# 三行四列的矩阵

for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()

for i in range(0, 9):
    for j in range(i):
        print('*', end='\t')
    print()

# 9*9乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', j * i, end='\t')
    print()
