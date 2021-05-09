# 打印水仙花数 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）

for item in range(100, 1000):
    single = item % 10
    ten = item // 10 % 10
    hundred = item // 100
    if single ** 3 + ten ** 3 + hundred ** 3 == item:
        print(item)

