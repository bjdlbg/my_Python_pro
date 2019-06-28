"""
网站判断用户身份标识，封禁IP怎么办？
    模拟浏览器，更改userAgent。
    换ip，设置代理，ip代理网站：访问代理ip网站，由代理
    登陆验证
"""
import requests
from bs4 import BeautifulSoup

#通过设置ip代理，上服务器监听到假的ip
#
proxies={
    #使用IP以及Port去访问网站，
    # "http":"http://Ip:port"
    "http":"http://60.9.1.81:80",
}
# print(proxies.get("http"))
response=requests.get("http://ip.tool.chinaz.com/",proxies=proxies)
html=BeautifulSoup(response.text,features="html.parser")
ipaddress=html.find("dd",attrs={"class":"fz24"}).text
print("您当前ip为",ipaddress)
# 1.194.187.4