# 类方法：针对类对象定义的方法
# 语法如下：
# @classmethod
# def 类方法名(cls):
#     pass
# 类方法需要用类修饰器@classmethod来表示，告诉解释器这是一个类方法


class Tool(object):

    # 使用赋值语句定义类属性，
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 让类属性值+1
        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("榔头")
Tool.show_tool_count()
