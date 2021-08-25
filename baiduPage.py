# 爬虫：通过编写程序来获取到互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个地址，从该网志中获取到资源或者内容

from urllib.request import urlopen

url = "https://baidu.com"
res=urlopen(url)

with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(res.read().decode("utf-8"))
print("over")