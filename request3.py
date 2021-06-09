import requests

url="https://movie.douban.com/j/search_subjects"

# 封装参数
param = {
    "type":"movie",
    "tag":"热门",
    "page_limit": 50,
    "page_start": 0
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
r=requests.get(url, params=param,headers=headers)
print(r.json())
r.close()

# 查看请求完整路径
# print(r.request.url)