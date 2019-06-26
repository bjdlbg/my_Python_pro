import requests
#爬虫与反爬
headers ={
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
try:
    response =requests.get("https://www.w3cschool.cn/java/java-collections.html")
    response.encoding = "utf-8"
    with open("result.html","w",encoding="utf8") as f:
        f.write(response.text)
except Exception as  e:
    print(e)

