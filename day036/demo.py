# 统计字符串中指定字符的个数

def getCount(str, ch):
    count = 0
    for item in str:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    a = getCount("hello", 'a')
    print(a)
