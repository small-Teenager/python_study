class Student:
    native_pace = 'china'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("调用父类构造函数")

    def show(self):
        print(self.__name, self.__age)

    def eat(self):
        print('吃饭')

    def play(self):
        print('play')

    # 静态方法
    @staticmethod
    def staticMethod():
        print('这是一个静态方法')

    @classmethod
    def classMethod(cls):
        print('这是一个类方法')


print(type(Student), id(Student), Student)

Student.staticMethod()

stu = Student('张飞', 18)

stu.eat()
stu.play()
stu.show()

# 类属性调用
print(Student.native_pace)

Student.native_pace = 'mainland'

print(Student.native_pace)
