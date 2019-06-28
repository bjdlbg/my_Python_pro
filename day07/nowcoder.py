import csv
import requests
from bs4 import  BeautifulSoup
#首先爬取整个牛客网页
respnose=requests.get("https://www.nowcoder.com/school/schedule")
print(respnose.text)#打印出来
html=BeautifulSoup(respnose.text,features="html.parser")
#找到节点<div class="act-main">
main=html.find("div",attrs={"class":"act-main"})
messageAll=main.find_all("div",attrs={"class":"act-company-body"})
#新建csv文件
with open("nowcoder.csv", "w", newline="")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["公司名称", "内推", "网申","笔试","面试","offer"])

if len(messageAll)>1:
    for m in messageAll:
        #print(m.text)
        title=m.find("h2").text
        recommend=m.find("div",attrs={"class":"act-company-info meeting"})
        re=recommend.text
        net=m.find("div",attrs={"class":"act-company-info resume"})
        ne=net.text
        exam=m.find("div",attrs={"class":"act-company-info written"})
        ex=exam.text
        face=m.find("div",attrs={"class":"act-company-info audition"})
        fa=face.text
        offer=m.find("div",attrs={"class":"act-company-info send-offer"})
        of=offer.text


        #print(title,recommend,net,exam,face,offer)
        # if title!=None or recommend!=None or net!=None or exam!=None:
        #     csv_writer.writerow([title,re,ne,ex,fa,of])
        # else:
        #     if recommend == None:
        #         re = "暂未开始"
        #     elif net == None:
        #         ne = "暂未开始"
        #     elif exam == None:
        #         ex = "暂未开始"
        #     elif face == None:
        #         fa = "暂未开始"
        #     elif offer == None:
        #         of = "暂未开始"
        #     csv_writer.writerow([title, re, ne, ex, fa, of])
else:
    print("爬取完毕")

# #名字
# title=main.find_all("h2")
# #内推
# meetingTime=main.find_all("div",attrs={"class":"act-company-info meeting"})
# #网申
# resumeTime=main.find_all("div",attrs={"class":"act-company-info resume"})
# #笔试
# writtenTime=main.find_all("div",attrs={"class":"act-company-info written"})
# #面试
# auditionTime=main.find_all("div",attrs={"class":"act-company-info audition"})
# #offer
# offerTime=main.find_all("div",attrs={"class":"act-company-info send-offer"})
# with open("nowcoder.csv", "w", newline="")as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(["公司名称", "内推", "网申","笔试","面试","offer"])
# if len(title)>1:
#     for t in title:
#         print(t.text)
#         csv_writer.writerow([])

# if len(meetingTime)>1:
#     for m in meetingTime:
#         print(m)


