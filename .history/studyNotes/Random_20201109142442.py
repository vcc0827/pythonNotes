import  numpy as np
import random
class ClassGenerator:
  nn = ["a", "b", "c", "d"]
  verb = ["只买","都买"]

  def popGet(self):
    nn_num = int(np.random.uniform(0, 4))  #允许生成其中多项
    assert nn_num <= 4
    nn_group_number = [random.randint(0, 3) for i in range(nn_num)]
    nn_group = []
    for i in range(nn_num):
      k = nn_group_number[i]
      nn_group = "".join(nn_group) + self.nn[k]
    return "".join(nn_group)
  
  def verbGet(self):
    ver_num = int(np.random.uniform(0,2)) #只随机生成其中一项
    return self.verb[ver_num]

  def coll(self):
    n = self.popGet()
    v = self.verbGet()
    return v+n
n = 0
while (n<100):
      gen = ClassGenerator()
      s = gen.coll()
      print(s)
      n = n + 1

