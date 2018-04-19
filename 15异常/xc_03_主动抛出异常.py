# 异常的传递：当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方，
# 如果传递到主程序，任然没异常处理，程序才会被终止


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序中增加异常捕获
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" %result)