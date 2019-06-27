import csv
import time

import requests
from bs4 import BeautifulSoup
index=1
with open("baby.csv", "w", newline="")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["编号", "标题", "超链接"])
    while True:
        if index == 1:
            url="http://www.shuaia.net/meinv/index.html"
        else:
            url="http://www.shuaia.net/meinv/index_"+str(index)+".html"
        response=requests.get(url)
        if response.status_code==404:
            break
        else:
            html=BeautifulSoup(response.text,features="html.parser")
            content=html.find("div",attrs={"id":"content"})
            divs=content.find_all("div",attrs={"class":"item masonry-brick"})
           # for div  in divs:
                #title=div.find("h2",attrs={"class":"item-title"}).text

