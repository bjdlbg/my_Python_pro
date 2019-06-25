"""
IO操作
内存->临时存储
磁盘->永久存储
    1.建立和一个文件的连接句柄
    2.读取或者写入文件
    3.释放文件句柄
"""

#exp1 读取文件

filehandler =open("data.txt",encoding="utf8")
content=filehandler.read()
filehandler.close()
print(content)

#写入文件

for i in range(1,11):
    filehandlerTemp=open("data"+str(i)+".txt",mode="w",encoding="utf8")
    filehandlerTemp.write(content)
    filehandlerTemp.write("IO操作需要三个流程：\n        1.建立文件句柄 "
                          "\n        2.读取或者写入为文件"
                          "\n        3.关闭文件句柄")
    filehandlerTemp.close()