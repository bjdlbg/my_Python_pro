import requests
from bs4 import BeautifulSoup
import time
import csv
import os
index = 1
rownum = 1
with open("baby.csv","w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["编号","标题","超级链接","评论数","点赞数"])
    while True:
        time.sleep(0.5)
        if index == 1:
            url = "http://www.shuaia.net/zhengtai/index.html"
        else:
            url = "http://www.shuaia.net/zhengtai/index_"+str(index)+".html"
        response = requests.get(url)
        response.encoding="utf-8"
        if response.status_code == 404:
            print("爬取完毕=====================")
            break
        else:
            index += 1
            html = BeautifulSoup(response.text,features="html.parser")
            content = html.find("div",attrs={"id":"content"})
            divs = content.find_all("div",attrs={"class":"item"})
            for div in divs:
                title = div.find("h2", attrs={"class":"item-title"})
                if not title:
                    titlestr = "没有标题"
                else:
                    titlestr =title.text
                img = div.find("img",attrs={"class":"attachment-weiran"})
                if not img:
                    srcstr = "没有"
                else:
                    srcstr = img.attrs["src"]
                    if os.path.exists("小帅哥图片"):
                        pass
                    else:
                        os.mkdir("小帅哥图片")
                    try:
                        imgresponse = requests.get(srcstr)
                        with open("小帅哥图片/" + titlestr + ".jpg", "wb") as f:
                            f.write(imgresponse.content)
                    except Exception as e:
                        print(e)
                comment= div.find("a",attrs={"class":"item-comment-count ds-thread-count"})
                if not comment:
                    commentstr= "没有信息"
                else:
                    commentstr = comment.text
                heart_no = div.find("span",attrs={"class":"heart-no"})
                if not heart_no:
                    heart_no_str = "没有信息"
                else:
                    heart_no_str = heart_no.text
                print([rownum, titlestr, srcstr, commentstr, heart_no_str])
                rownum += 1


"""
分析源码
需要注意有没有item-main这个div 
没有的话需要处理
"""