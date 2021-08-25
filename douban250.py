# 拿到页面源代码
# 通过re来提取想要的有效信息 re

import requests
import re
import csv

url ="https://movie.douban.com/top250"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
resp = requests.get(url,headers=headers)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)'
                 r'</span>.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<number>.*?)人评价</span>', re.S)
res=obj.finditer(page_content)
f=open('douban250.csv',mode="w",encoding="utf-8",newline='' )
csvwriter = csv.writer(f)
for item in res:
    # print(item.group('title'))
    # print(item.group('year').strip()) #为了去除空格
    # print(item.group('score'))
    # print(item.group('number'))
    dic = item.groupdict()
    dic['year']=dic['year'].strip()
    csvwriter.writerow(dic.values())
resp.close()
f.close()
print('over')
