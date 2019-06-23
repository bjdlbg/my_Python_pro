""""
函数：为了完成特定的工作进行 代码封装
"""
#计算1-100累加
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

def getSum(endpoint):
    sum=0
    for i in range(1,endpoint):
        sum+=i
    print(sum)

""""
有默认值的函数
"""
def my_print(name="匿名用户"):
    print("特朗普",name)

getSum(2333)
my_print()

def sayHello(*args):
    for human in args:
        print("hello",human)
sayHello("1","2")

"""
普通形参
带有默认值的形参
普通形参，可变元祖形参
普通形参，可变元祖形参，可变字典形参
"""

def sayHello2(a,b,*args,**kwargs):
    print(type(kwargs),kwargs)
    for i in  range(1,len(args)):
        print(i)
    print(a+b)
sayHello2(100,50,1,2,3,mame="heda",address="kaifeng")

"""
我是：name
我要告诉下列人员：*args
告诉他们河大的信息：**kwargs
"""
def tellMessage(name,*args,**kwargs):
    msg=""
    for key,value in kwargs.items():
        print(key,value                                  )
    for people in args:
        print("你好",args[people],"我是",name,
              "\n我要告诉你河大信息",kwargs)
tellMessage("光头强","李老板","熊二","熊大","吉吉国王",
            message1="我电锯被偷了",message2="是不是你干的",message3="我现在要去揍你")

