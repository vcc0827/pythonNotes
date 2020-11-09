import  numpy as np
import random
class ClassGenerator:
    Adj = ["蓝色的","好看的","小小的","年轻的"]
    verb = ["看着","听着","看见","听见"]
    noun = ["女人","小猫","篮球","桌子"]
    Article = ["一个","这个"]

    def AdjGet(self):
        Adj_num = int(np.random.uniform(0, 4))  #形容词数量
        assert Adj_num<=4
        print("the num of adj is",Adj_num)
        adj_group_number =[random.randint(0,3) for i in range(Adj_num)]                            #list(np.random.uniform(0,4,Adj_num))  #形容词序号列表    np的随机函数返回的是ndarry多维数组
        #print(adj_group_number.shape)
        adj_group = []
        for i in range(Adj_num):
            k =adj_group_number[i]
            adj_group = "".join(adj_group)+self.Adj[k]
        return "".join(adj_group)               #list转字符串

    def verb_phrase_Gene(self):
        verb_num = int(np.random.uniform(0, 4))
        noun_num = int(np.random.uniform(0, 4))
        return self.verb[verb_num]+self.noun[noun_num]

    def noun_phrase_gene(self):
        Article_num = int(np.random.uniform(0, 2))                 #np.random.uniform取值左右都闭，且返回值是float64类型！
        Adj_Group = self.AdjGet()
        noun_num = int(np.random.uniform(0, 3))
        return self.Article[Article_num]+Adj_Group+self.noun[noun_num]


    def sentGene(self):
        noun_phr = self.noun_phrase_gene()
        verb_phr = self.verb_phrase_Gene()
        return noun_phr+verb_phr

while(1):
    key = input("生成语句？Y|N")
    if key == 'Y':
        print(">>generate(\"sentence\")")
        generate = ClassGenerator()
        sentence = generate.sentGene()
        print(sentence)
    if key =='N':
        break