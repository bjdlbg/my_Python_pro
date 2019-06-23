class People:
    def __init__(self,_name,_age,_addr):
        self.name=_name
        self.age=_age
        self.addr=_addr
        self.score=None

    def getinfo(self):
        return {"姓名":self.name,"年级":self.age,"老家":self.addr}
    def getscore(self):
        return {"姓名":self.name,"分数":self.score}
    def setscore(self,_score):
        self.score=_score

p1=People("奥巴马",12,"纽约")
p2=People("小布什",19,"洛杉矶")

p1.setscore(598)
p2.setscore(234)

_1scor=p2.getscore()
_2scor=p1.getscore()

print(_1scor,_2scor)