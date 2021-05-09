# 条件表达式
num_a = int(input('请输入第一个整数\n'))
num_b = int(input('请输入第二个整数\n'))
if num_a >= num_b:
    print(num_a, '大于等于', num_b)
else:
    print(num_a, '小于', num_b)

# 条件表达式比较
print((num_a, '大于等于', num_b) if num_a >= num_b else (num_a, '小于', num_b))
