import  numpy as np
import random
class ClassGenerator:
  nn = ["香水", "项链", "口红", "神仙水"]
  verb = ["买"]

  def popGet(self):
    nn_num = int(np.random.uniform(1, 4))  #允许生成其中多项
    assert nn_num <= 4
    nn_group_number = [random.randint(1, 3) for i in range(4)]
    nn_group = []
    for i in range(nn_num):
      k = nn_group_number[i]
      nn_group = "".join(nn_group) + self.nn[k]
    return "".join(nn_group)
  
  def verbGet(self):
   # ver_num = int(np.random.uniform(0,1)) #只随机生成其中一项
    return self.verb[0]

  def coll(self):
    n = self.popGet()
    v = self.verbGet()
    return v + n
while (1):
  key = input("是否让做出选择 Y/N?  ")
  if key == 'y':
    n = 0
    while (n<1314):
      gen = ClassGenerator()
      s = gen.coll()
      print(s)
      n = n + 1
      if key == 'n':
       break
