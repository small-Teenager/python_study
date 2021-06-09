# 水仙花数字
import math

for i in range(100, 999):
    bai = i % 10

    shi = i // 10 % 10
    ge = i // 100
    if math.pow(ge, 3) + math.pow(shi, 3) + math.pow(bai, 3) == i:
        print(i)
