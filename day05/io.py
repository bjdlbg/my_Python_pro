"""
with 可以声明局部用于对象自动释放
    close自动调用
"""

try:
    with open("E:\\新建文件夹\\14004_42eca4efb5.jpg", mode="rb") as f:
        content = f.read()
        for i in range(1, 10):
            with open("tmp" + str(i) + ",jpg", mode="wb") as f2:
                f2.write(content)
except FileExistsError as e:
    print("图片未找到",e)
