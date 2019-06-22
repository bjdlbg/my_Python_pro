""""
创建一个列表
随机向列表中插入10个 50~100的整数
"""
import random

list1=[]
for r in range(10):
    num=random.randrange(50,100)
    list1.append(num)
print(list1)

while True:
    listLen=len(list1)
    if listLen>0:
        #随机一个索引
        index =random.randrange(0,listLen)
        element =list1.pop(index)
        print("删除了：",element)
    else:
        print("清空了..")
        print(list1)
        break
""""
字典：键值对 查询快
"""
d1={}
print(type(d1))# 默认为字典

#键为不可变数据类型，集合不可以作为键
d2={"name":"henu","addr":"kaifeng"}
d2["people_num"]=50000
d2[10]=1000
d2[(10,20)]="hiworld"
print(d2)
result=d2.pop("name")
print("删除掉name",d2)

#获取开封对应的value
print(d2.get("addr"))

#遍历map
for key in d2.keys():
    print(key)