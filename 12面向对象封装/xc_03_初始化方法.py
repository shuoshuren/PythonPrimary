
class Cat:

    def __init__(self):
        print("初始化方法")
        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" %self.name)



# 使用类名()创建对象的时候，python会自动调用“__init__()”
tom = Cat()
tom.eat()
print(tom.name)