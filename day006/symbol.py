# 算数运算符
print(1+1)
print(1-2)
print(3*4)
print(2/5) # 除法
print(11//2) # 整除运算
print(11%2) # 取余运算
print(2**3) # 2的3次方

# 一正一负 向下取整
print(-11//2)
print(11//-2)
print(-11//-2)

# 赋值运算符
a=3+4
print(a)
a=b=c=20 # 链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

# 参数赋值
a=20
print(a,id(a))
a+=30
print(a,id(a))
# 解包赋值
a,b,c=2,3,4
print(a,b,c,id(a),id(b),id(c),type(a),type(b),type(c))

# swap 解包赋值
a,b=7,8
# 交换前
print(a,b,id(a),id(b),type(a),type(b))
# 交换后
a,b=b,a
print(a,b,id(a),id(b),type(a),type(b))

# 比较运算符 比较的是值,value
a,b=10,20
print('a>b?',a>b)
print('a<b?',a<b)
print('a<=b?',a<=b)
print('a>=b?',a>=b)
print('a=b?',a==b)
print('a!=b?',a!=b)

print('a',b,id(a),id(b))
print('a is b',a is b) ## a,b的标识不一致
c,d=1,1
print('a',b,id(c),id(d))
print('c is d',c is d) ## c,d的标识一致

list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1==list2)
print(list1 is list2)
print(list1 is not list2)
print(list2,list2,id(list1),id(list2))

# 布尔运算符 and , or , not, in, not in
a,b=1,2
print(a==1 and b==2) # true
print(a==1 and b<2) # false
print(a!=1 and b==2) #false

print(a!=1 or b==2) #true

f=True
f2=False
print(not f) # false
print(not f2) #true

str="hello world!"
print("he" in str)
print("he" not in str)


# 位运算符











