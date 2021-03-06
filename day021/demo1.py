# 字符串的创建和驻留机制
# 仅保存一份相同且不可变字符串的方法,
# 不同的值被放在字符串的驻留池中，对相同的
# 字符串只保留一份拷贝，后续的连续创建，不会开辟新空间，
# 而是把该字符串的地址赋值给新创建的变量
str1 = 'python'
str2 = "python"
str3 = '''python'''
print(str1, id(str1))
print(str2, id(str2))
print(str3, id(str3))
# 字母_数字_下划线

# 优点
'''
    当需要值相等的字符串时，可以直接从字符串池中拿来使用，
避免频繁创建和销毁，提升效率和节约内存，因此拼接字符串和修改
字符串会比较影响性能。
    当进行字符串拼接时，建议使用str类型的join方法，而非+
因为join()方法是先计算出所有字符中的长度，然后在拷贝，
只new一次对象，效率要比+高
'''