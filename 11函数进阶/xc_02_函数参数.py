

def demo1(num,list):
    print("函数内部执行")
    # 在函数内部针对函数参数赋值，不会影响到外部实参
    num = 100
    list = [1,2,3]
    print("num:%d" %num)
    print("list:%s" %list)
    print("函数执行完毕")

def demo2(list):
    print("函数内部执行")
    # 在函数内部使用方法修改可变参数的值，会影响到外部实参
    # 列表变量 +=操作等于extend
    list.append(9)
    print("list:%s" %list)
    print("函数执行完毕")



gl_num = 10
gl_list = [4,5,6]
demo1(gl_num,gl_list)
print("num:%d" %gl_num)
print("list:%s" %gl_list)

demo2(gl_list)
print("list:%s" %gl_list)
