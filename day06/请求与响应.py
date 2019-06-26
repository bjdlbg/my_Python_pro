import requests
try:
    response = requests.get(
        "https://bjdlbg.github.io/images/SAO.jpg"
    )
    if response.status_code==200:
        with open("sao.jpg", "wb") as j:
            j.write(response.content)
except Exception as e:
    print("失败了：",e)