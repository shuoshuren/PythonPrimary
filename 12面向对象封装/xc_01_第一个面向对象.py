

class Cat:
    def eat(self):
        print("小猫爱吃鱼")


    def drink(self):
        print("小猫要喝水")


# 创建对象
tom = Cat()

tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print(tom)
print(lazy_cat)

addr = id(tom)

print("%x" %addr)