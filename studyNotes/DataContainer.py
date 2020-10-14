####**数据容器**####
# ***列表***
List1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ["a", "b", "c"], 11]
# 获取列表指定元素的方法 List1[]
print(List1[2:5])  # [start:end] 从start开始（包含）到end结束（不包含）
print(List1[2])  # 获取列表索引为2的元素
print(List1[2:100])  # 当索引中end大于列表长度则相当于end是列表末尾
print(List1[-9])  # 当索引为负数表示倒序 不可超过列表长度
print(List1[9:1])  # 当开始索引大于结束索引 默认返回空列表[]
print(List1[10][0])  # 取嵌套列表元素
# 列表运算 加、乘
l1 = [1, 2]
l2 = [3, 4, 5, 3, 2, 1, 3, 2, 56]
l3 = l1 * 2
print(l1 + l2)  # 列表加运算即为拼接列表
print(l3)  # 列表乘运算即为复制元素并拼接成新列表（并不是对列表内元素进行乘法运算）
# 列表其他操作方法
l1.append(-2)  # 末尾增加一个元素
l1.insert(1, 11)  # (指定位置索引，元素)在列表指定位置插入元素
l4 = [13, 14, 15]
l1.extend(l4)  # 末尾增加多个元素
l1.pop()  # 删除最后一个
l1.pop(0)  # 删除指定索引位置的元素
l1.remove(-2)  # 删除指定值的元素
l1.clear()  # 清空列表
l2.sort()  # 升序排序（列表元素须为同一种数据类型
l2.reverse()  # 列表元素反序
print("l2:", l2)
print(l2.index(3))  # 显示该实际值元素第一次出现的位置
print(l2.count(3))  # 统计该实际值元素出现次数
l22 = l2.copy()  # 复制列表
print(l22)
# 字符串转列表
speech = "你们啊,不要总是想着搞个大新闻,中国有句古话,叫闷声发大财,识得唔识得啊"
l4 = list(speech)
print("l4", l4.count(","))
# 列表推导
l5 = [i for i in range(10)]  # range(n) 从0开始的n个数的集合
print("l5", l5)
l6 = [i + 1 for i in range(10)]
print("l6", l6)

# demo 有list b=[23,45,22,44,25,66,78]
# 1.生成奇数列表 2.输出[25,47,24,46,27,68,80]
b = [23, 45, 22, 44, 25, 66, 78]
oddList = []
for i in b:
    if i % 2 != 0:
        oddList.append(i)
add2 = [i+2 for i in b]
print(oddList)
print(add2)


# ***元组***
# 定义：类似列表，但是创建后无法对其中的元素进行添加删除或修改操作。元组不可更改
z1 = ()  # 创建空元组
z2 = (1, 9, 2, 6)  # 直接创建元组
z3 = tuple([1, 9, 2, 6])  # 从数组中创建
print(z3)
z4 = tuple("另请高明")  # 从字符串创建
z5 = '另', '请', '高', '明'  # 通过,分割 创建的元组与z4同
# ----元组本身不可更改但是元组中的“列表”中的元素可以更改
z6 = (1, 2, 3, [4, 6, 6])
print(z6)
z6[3][1] = 5
print(z6)


# ***字典***
# 描述：字典由键值对构成。 键：必须是不可更改的数据类型，可以使用字符串、数值，但是列表和字典不可以作为字典的键。值：可以为任何数据类型。
warrior = {
    "judge": "judgeValue",
    "crystal": "crystalValue",
    "lina": 1+2
}
hero = warrior.copy()  # 复制字典
warrior.clear()  # 清空
print(hero.get("judge"))  # 返回指定键的值，查不到返回None
print(hero.items())  # 遍历字典并以列表形式返回元组数组
print(hero.keys())  # 以列表形式返回对应字典的键
print(hero.values())  # 以列表形式返回字典的值

# demo 信息管理系统
# 1.定义2个同学：
# 姓名：李明，年龄25，考试分数：语文80，数学75，英语85
# 姓名：张强，年龄23，考试分数：语文75，数学82，英语78
# 2.添加一门课程A 成绩 李明60分，张强：80分。  3.张强的数学成绩从82分改为89分 4.删除李明的年龄数据。 5.对张强同学的课程分数按照从低到高排序输出。
sys = []
stu = {
    "name": "", "age": "", "yw": "", "sx": "", "yy": ""}
for i in range(2):
    rp = stu.copy()
    if i == 0:
        rp["name"] = "李明"
        rp["age"] = 25
        rp["yw"] = 80
        rp["sx"] = 75
        rp["yy"] = 85
    sys.append(rp)
    if i == 1:
        rp["name"] = "张强"
        rp["age"] = 23
        rp["yw"] = 75
        rp["sx"] = 82
        rp["yy"] = 78
print("1.系统：")
for i in sys:
    if (i.get("name") == "李明"):
        i["A"] = 60
    if (i.get("name") == "张强"):
        i["A"] = 80
print("2.新增一门课程后的系统：", sys)
for i in sys:
    if (i.get("name") == "张强"):
        i["sx"] = 89
    if (i.get("name") == "李明"):
        del i["age"]
print("3.改分数：", sys)
print("4.删年龄：", sys)
sortStu = []
for i in sys:
    if (i.get("name") == "张强"):
        sortStu.append(int(i.get("yw")))
        sortStu.append(int(i.get("sx")))
        sortStu.append(int(i.get("yy")))
        sortStu.append(int(i.get("A")))
sortStu.sort()
print("5.成绩升序：",sortStu)
