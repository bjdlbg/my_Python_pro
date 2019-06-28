"""
一、爬去百思不得姐
    将以下数据存入CSV或者MongoDB
    发帖人名字，头像图片地址，发帖时间，文字描述，主图地址，
    点赞数，差评数，评论数。


html界面分析：
    每个网页含有两个帖子列表结构为：
        .
        .
        <div class="j-r-c">
            # 第一个列表
            <div class="j-r-list">
                <ul>（target）
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>

            # 第二个列表 (往日神贴)
            <div class="j-r-list">

            </div>
        </div>
        .
        .
"""


import requests
from bs4 import BeautifulSoup
import time
import csv
#每页10个item
desId=0
#页数
index=1
#编号
rowNum=0
#新建文件来存取爬来的数据（图片均为地址）
with open("budejiedata.csv","w",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["编号","昵称","头像","时间","描述","主图","点赞数",
                         "差评数","分享数","评论数"])
    while True:
        #time.sleep(0.2)#设置爬取间隔
        #页数判别(总页数为50)
        url="http://www.budejie.com/pic/"+str(index)
        response = requests.get(url)
        response.encoding = "utf-8"
        #爬取数据
        if response.status_code == 404:
            print("-------------- 爬取完毕 ---------------")
            break
        else:
            index += 1
            html = BeautifulSoup(response.text,features="html.parser")
            content = html.find("div",attrs={"class":"j-r-list"})#该标签包含所有li
            div=content.find_all("div",attrs={"class":"j-list-user"})
            div2 = content.find_all("div", attrs={"class": "j-r-list-tool"})
            imags=content.find_all("div",attrs={"class":"j-r-list-c-img"})
            if not div2:
                print("没找到描述块")
            # div=content.find_all("li")
            for l in div:
                #昵称
                name=l.find("a",attrs={"class":"u-user-name"}).text
                #头像链接
                head=l.find("img",attrs={"class":"u-logo lazy"})
                headSrc=head.attrs["data-original"]
                #时间
                tdiv=l.find("div",attrs={"class":"u-txt"})
                time=tdiv.find("span",attrs={"class":"u-time f-ib f-fr"}).text
                #帖子描述
                describe=l.find("div",attrs={"class":"j-r-list-c-desc"})
                if not describe:
                    describeMsg = "没有描述"
                else:
                    describeMsg = describe.text
                #主图
                # pic=l.find("a",attrs={"class":"lazy"})
                # if not pic:
                #     picAddr="没有图片"
                # else:
                #     picAddr=pic.attrs["src"]
                rowNum += 1
                #控制第二个div中数据
                if desId>=10:
                    desId=0
                print(rowNum, name, "头像：", headSrc)
                print(div2[desId].attrs["data-title"])
                print("点赞数：", div2[desId].find("span").text)
                print("踩数：", div2[desId].find("li",attrs={"class":"j-r-list-tool-l-down"})
                      .find("span").text)
                #comment-counts
                print("评论数：",div2[desId].find("span",attrs={"class":"comment-counts"}).text)
                print(time)
                print("主图：",imags[desId].find("img").attrs["data-original"])
                print("当前是第：",index,"页数")

                desId += 1





# response=requests.get("http://www.budejie.com/pic")
# with open("temp.html","w",encoding="utf8")as f:
#     f.write(response.text)
