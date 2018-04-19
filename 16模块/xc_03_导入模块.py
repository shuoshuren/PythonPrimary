import xc_01_测试模块1 as DogModule
from xc_02_测试模块2 import Cat



# 模块别名采用大驼峰命名法

# 如果两个模块存在同名的函数，那么后导入的函数会覆盖先导入的模块
# 如果发现存在同名的函数，可以通过as 起别名

# 模块.__file__:获取模块文件路径

# 原则：每一个文件都应该是可以被导入的
# 在导入时，模块文件任何没有缩进的代码都会被执行

# __name__属性：测试模块的代码只在测试情况下被运行，而在被导入时不会被执行
# __name__是python的内置属性，记录着一个字符串，如果是被其他文件导入的，__name__就是模块名
# 如果是当前执行的程序，__name__就是"__main__"
dog = DogModule.Dog()
print(dog)

cat = Cat()
print(cat)
print( DogModule.__file__)