"""
一、新建task1.py
    使用with open 方法将图片复制十张 名字为1-10
"""
try:
    with open("tmp1.jpg", mode="rb") as f:
        content = f.read()
        for i in range(1, 11):
            with open( str(i) + ",jpg", mode="wb") as f2:
                f2.write(content)
except FileExistsError as e:
    print("图片未找到",e)