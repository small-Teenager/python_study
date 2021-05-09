# 流程控制 break and continue

for item in range(3):
    pwd = input('请输入密码')
    if pwd == '888':
        print('密码正确！')
        break
    else:
        print('密码错误')

a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '888':
        print('密码正确！')
        break
    else:
        print('密码错误')
    a += 1

# 输出1-50 5的倍数
item = 0
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

for item in range(1, 51):
    if item % 5 != 0:
        continue
    else:
        print(item)
