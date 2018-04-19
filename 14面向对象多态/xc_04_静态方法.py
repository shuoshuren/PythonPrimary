# 静态方法：不访问实例属性或者类属性
# 语法格式：
# @staticmethod
# def 静态方法():
#     pass
# 静态方法需要用@staticmethod修饰器标识，告诉解释器下面的方法是静态方法
# 通过类名.调用静态方法,不需要创建对象


class Dog(object):

    @staticmethod
    def run():
        print("小狗快跑")


Dog.run()