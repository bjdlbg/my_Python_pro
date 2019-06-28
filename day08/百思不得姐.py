"""
一、爬去百思不得姐
    将以下数据存入CSA或者MongoDB
    发帖人名字，头像图片地址，发帖时间，文字描述，主图地址，
    点赞数，差评数，评论数。
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
with open("aisidata.csv","w",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["编号","昵称","头像","时间","描述","主图","点赞数",
                         "差评数","分享数","评论数"])
response=requests.get("http://www.badejie.com/pic/1")
with open("temp.txt","w")as f:
    f.write(response.text)
