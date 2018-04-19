class Cat:

    def __init__(self,name):
        print("初始化方法")
        # self.属性名 = 属性的初始值
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" %self.name)


tom = Cat("大懒猫")
tom.eat()