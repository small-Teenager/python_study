# 计算圆的面积和周长
import math


class Circle(object):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r


if __name__ == '__main__':
    r = 3
    c = Circle(r)
    print('周长', c.get_perimeter())
    print('面积', c.get_area())
