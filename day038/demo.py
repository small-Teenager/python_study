# 3边能否组成三角形

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception('三角形的边必须是正数！')
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


if __name__ == '__main__':
    try:
        print(is_triangle(0, 2, 3))
    except Exception as e:
        print(e)

        print(is_triangle(1, 2, 3))
        print(is_triangle(3, 4, 5))
