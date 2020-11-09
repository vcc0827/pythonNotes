import  numpy as np
import random
class ClassGenerator:
  nn = ["a", "b", "c", "d"]
  
  def nnGet(self):
    nn_num = int(np.random.uniform(0, 4))
    return self.nn[nn_num]
  
while (1):
    key = input("是否生成？Y|N")
    if key == 'Y' :
      gen = ClassGenerator()
      s = gen.nnGet()
      print(s)
    if key == 'N':
      break

