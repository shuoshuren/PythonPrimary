# 多值参数：函数参数个数是不确定的
# Python中有两种多值参数：
# 参数名前面加一个×，可以接收元组，
# 参数名前面加两个*，可以接收字典
# 一般在给多值参数命名时，习惯使用以下两个名字
# ×args---存放元组参数，前面一个×、
# **kwagrs--存放字典参数，前面两个×

def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1,2,3,4,5,name="小明",gender=True,age=18)

gl_nums = (1,2,3)
gl_dict = {"name":"小明","gender":True,"age":18}

# 元组和字典的拆包
# 在调用多值参数的函数时，如果希望直接将一个元组变量传递给*args.一个字典变量传递给**kwargs.就可以使用拆包，
# 拆包的方法是：在元组变量前面，添加一个*，在字典变量前面，添加两个*
demo(9,*gl_nums,**gl_dict)