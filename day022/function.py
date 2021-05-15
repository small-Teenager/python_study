# 函数的创建和调用
'''
函数：是执行特定任务和以完成特定功能的一段代码
为什么使用函数
    复用代码
    隐藏实现细节
    提高维护性
    提高可读性便于调试
'''


def calc(a, b):
    c = a + b
    return c


result = calc(10, 3.40)
print(result)


def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print(fun([0, 1, 2, 3, 4, 5, 6, 7]))

'''
函数的返回值
1.如果函数没有返回值(函数执行完毕之后，不需要给调用处提供数据) return 可以省略不写
2.函数的返回值，如果是1个，直接返回类型
3.函数的返回值，如果是多个，返回的结果为元组
'''

'''
函数的参数定义
'''


# 定义默认值
def fun(a, b=10):
    return a + b


print(fun(3))  # 13
print(fun(3, 4))  # 7


# 可变参数定义
def funVariableParameters(*args):
    print(*args)


funVariableParameters(3)
funVariableParameters(3, 4, 5)
