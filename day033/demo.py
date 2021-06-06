# Base conversion

def conversion():
    num = int(input("请输入一个十进制的整数\n"))

    print(num, '的二进制为:', bin(num))

    print(num, '的八进制为:', oct(num))

    print(num, '的十六进制为:', hex(num))


if __name__ == '__main__':

    try:
        conversion()
    except:
        print('只能输入整数，请重新输入')
        conversion()
