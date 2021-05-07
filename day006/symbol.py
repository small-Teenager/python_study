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













