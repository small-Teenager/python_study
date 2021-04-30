import print as print

n1=90
n2=-76
n3=0
print(n1)
print(n2)
print(n3)

print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

# 浮点数相加
n1=1.1
n2=2.2
print(n1+n2) # 3.3000000000000003

from decimal import Decimal

print(Decimal("1.1")+Decimal("2.2")) #3.3

# bool
print(True+1) #2
print(False+1) #1

b1=True
b2=False
print(b1,type(b1))
print(b2,type(b2))

# str
str1='Python'
str2="Java"
print(str1,type(str1))
print(str2,type(str2))






