"""
mongodb
1.安装msi
2.卢瑟版本解压安装
对比mysql
    Mysql是一个关系型数据库管理系统
        数据库->表》行，列

    mongodb是一个非关系型数据库管理系统
        数据库-> 集合》文档，字段
        所有文档对象没有特定格式（没有特定的列）

python 如何连接mongodb
    安装pip install pymongo
"""
import pymongo
#1.获取连接实例
mongoClient = pymongo.MongoClient()
#2.指定数据库
db = mongoClient["test"]
#3.指定集合
col1 = db["new server test"]
#4.查找数据
result = col1.find()
for r in result:
    print(r)


#插入文档对象
col1.insert({"name":"金克斯","age":18,})


result2 = col1.find()
for r2 in result2:
    print(r2)