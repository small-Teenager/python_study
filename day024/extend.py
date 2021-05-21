# 继承

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0},年龄：{1}'.format(self.name, self.age))


# 定义子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score


# 定义子类
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        print('姓名：{0},年龄：{1},教龄：{2}'.format(self.name, self.age, self.teachofyear))


stu = Student('张飞', 18, '88')
stu.info()

print(stu.score)

teacher = Teacher('孔子', 18, 3)
teacher.info()
print(dir(teacher))
print(teacher)
