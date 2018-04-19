
# Python中的逻辑运算符包括：与and 或or 非not三种

age = 150

if age >= 0 and age <= 120:
    print("年龄是正确的")
else:
    print("年龄错误")

print("-"*30)

is_emple = False

if not is_emple:
    print("非本公司成员，不允许入内")