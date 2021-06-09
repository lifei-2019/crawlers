# 安装requests
# pip install requests

import requests
query = input("请输入想搜索的")
url=f'http://www.baidu.com/s?wd={query}'
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
res=requests.get(url, headers=headers)

# code为状态码，text网页源码
print(res.text)
res.close()