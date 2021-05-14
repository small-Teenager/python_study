# 字符串的常用操作
# 大小写转换
# upper() 小写转大写

str1 = 'hello world'
print(str1.upper())

# lower() 大写转小写
str2 = 'HELLO WORLD'
print(str2.lower())

# capitalize() 第一个字符转大写 ，其余字符转小写
str3 = 'hello world'
print(str3.capitalize())

# 每个单词第一个字符转大写 ，每个单词的剩余字符转小写
str4 = 'hello world'
print(str4.title())

# center() 居中对齐
str5 = "hello,world"
print(str5.center(20, '*'))

# ljust()
print(str5.ljust(20, '*'))

# rjust()
print(str5.rjust(20, '*'))

# zfill()
print(str5.zfill(20, '*'))


