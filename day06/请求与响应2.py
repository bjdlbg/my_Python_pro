
import requests
response =requests.get("https://www.w3cschool.cn/java/java-collections.html")
response.encoding="utf-8"
print(response.text)
with open("page1.html","w",encoding="utf8") as f:
    f.write(response.text)
