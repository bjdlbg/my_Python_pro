# import requests
# response = requests.get("https://quote.stockstar.com/stock/sha_3_1_1.html")
# print(response.text)

#安装bs4,数据清洗，可以自动补全html标签
# html=""
# from bs4 import BeautifulSoup
# newHtml = BeautifulSoup(html,features="html.parser")
import csv
import time

import requests
from bs4 import BeautifulSoup
# response = requests.get("https://quote.stockstar.com/stock/sha_3_1_1.html")
# print(response.text)
# html = BeautifulSoup(response.text,features="html.parser")
# #bs4中的find方法可以找到标签中节点
# tdoby=html.find("tbody",attrs={"id":"datalist"})
# trs = tdoby.find_all("tr")
try:
    with open("stock.csv","w",newline="")as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(["股票代码","股票名称","最新价格"])
        index =1
        while True:
            time.sleep(1)
            response = requests.get("https://quote.stockstar.com/stock/sha_3_1_"+str(index)+".html")
            print(response.text)
            html = BeautifulSoup(response.text, features="html.parser")
            # bs4中的find方法可以找到标签中节点
            tdoby = html.find("tbody", attrs={"id": "datalist"})
            trs = tdoby.find_all("tr")
            if len(trs)>1:
                for t in trs:
                    tds=t.find_all("td")
                    code=tds[0].text
                    name=tds[1].text
                    nowPrice=tds[2].text
                    #print("得到的股票信息","股票代码",code,"股票名称",name,"最新价格",nowPrice)
                    csv_writer.writerow([code, name, nowPrice])
                print("爬取完成第：",index,"页")
                index=index+1
            else:
                print("爬取了所有数据")
                break
except Exception as e:
    print(e)