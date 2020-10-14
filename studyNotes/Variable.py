# 变量variable
# 命名规则: 开头不能是数字，除特殊符号（不包括下划线_）、已有关键字外均可。
pie = 3.14159265358979323846
_pie = "pie"
AMDYes = True
print(pie)
print(_pie)
print(AMDYes)


# 字符串string
# 定义：单、双、三引号(triple single quotation marks)所包住的对象
print('too young')
print("too simple")
print('''sometimes naive''')


# 数值number
# 定义：整型、浮点、复数对象
j = 1926
int: j

z = 1926.0817
float: z

complex: 1900 + 26

print(j,type(j))
print(z,type(z))

# 布尔值bool
t, f = True, False
print('t and f', t and f)
print('t or f', t or f)
print('not f', not f)
print('not t != f',not t != f)
print(' t == f', t == f)


# 计算方式
# 加
jia = 19 + 26
print(jia)
# 减
jian = 19 - 26
print(jian)
# 乘
cheng = 8 * 17
print(cheng)
# 浮点除
fuchu = 5 / 2
print(fuchu)
# 整型除
zhchu = 5 // 2
print(zhchu)
# 指数
zhishu = 2 ** 10
print(zhishu)
# 余数
yushu = 1024 % 3
print(yushu)

# 多运算符有优先级次序

# 自增运算（不能写成i++形式
selfplus = 1
selfplus = selfplus + 1
selfplus += 1

# 类型转换
changer = 100
isinstance(changer, float)  #查看变量是否为猜测类型 格式isinstance(变量名，猜测类型)
print(isinstance(changer, float))
int()  #转整型
float()  #浮点
complex()  #复数
bool()  #布尔

a = input()
a = float(a)
b = 2
print(int(a) + b)


# # demo 计算圆柱体体积
# import math
# r = input()
# r = float(r)
# s = math.pi * r * r
# print(s)
