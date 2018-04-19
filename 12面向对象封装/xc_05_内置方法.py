class Cat:

    def __init__(self,name):
        print("初始化方法")
        # self.属性名 = 属性的初始值
        self.name = name

    # 析构函数
    def __del__(self):
        print("%s 要走了" %self.name)

    # 定制变量输出信息
    def __str__(self):
        return "{name:%s" %self.name +"}"

    def eat(self):
        print("%s 爱吃鱼" %self.name)


cat = Cat("Tom")
print(cat)