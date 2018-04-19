# 在开发时，应该把模块中所有的全局变量定义在所有的函数上方，就可以保证所有的函数都能够正常访问到每一个全局变量

gl_num = 10


def demo1():
    # 在Python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个同名的局部变量
    num = 20
    print("demo1 num:%d" % num)


def demo2():
    print("demo2 num:%d" % gl_num)

def demo3():
    """
    修改全局变量
    :return:
    """
    # global 关键字，告诉Python解释器变量是全局变量
    global gl_num
    gl_num = 30
    print("修改全局变量demo3 num %d" %gl_num)

demo3()
demo1()
demo2()
print("num:%d" %gl_num)