import traceback

# traceback 打印异常信息
try:
    a, b = 10, 0
    c = a / b
except:
    traceback.print_exc()
