# 分支结构
# 单分支结构
money = 200
s = int(input('请输入取款金额\n'))
if s <= money:
    money -= s
    print('取款成功，余额为:', money)

# 双分支结构
s = int(input('请输入数字\n'))
if s % 2 == 1:
    print(s, "是奇数")
else:
    print(s, "是偶数")

# 多分支结构
socre = int(input('请输入分数\n'))
if socre >= 90 and socre <= 100:
    print(socre, '是A')
elif socre >= 80:
    print(socre, '是B')
elif socre >= 70:
    print(socre, '是C')
elif socre >= 60:
    print(socre, '是D')
elif socre < 60 and socre >= 0:
    print(socre, '是E')
else:
    print(socre, "没有在[0,100]")

answer = input('您是会员吗？y/n\n')
money = float(input('请输入购物金额:\n'))
if answer == 'y':
    # print('会员')
    if money >= 200:
        print('打8折,付款金额:', money * 0.8)
    elif money >= 100:
        print('打9折,付款金额:', money * 0.9)
    else:
        print('不打折,付款金额:', money)
else:
    # print('非会员')
    if money >= 200:
        print('打9.9折,付款金额:', money * 0.95)
    else:
        print('不打折,付款金额:', money)
