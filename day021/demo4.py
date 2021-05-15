# 字符串的编码和解码
'''
编码 将字符串转换为二进制数据(bytes)
解码 将bytes类型的数据转换成字符串类型
'''

# 编码
s = '你好，世界'
# GBK编码中，一个中文两个字节
print(s.encode(encoding='GBK'))
# UTF-8编码中，一个中文三个字节
print(s.encode(encoding='UTF-8'))

# 解码
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
