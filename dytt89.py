# 最终目的为了获得吗每个电影下载地址

import requests
# 此处是因为加了verify=False会报waring
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
import csv

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
domain = "https://dytt89.com/"
resp = requests.get(domain,verify=False,)   #verify=False去掉安全验证
resp.encoding='gb2312' #指定字符集
# print(resp.text) 
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名　(?P<title>.*?)<br />'
                  r'.*?style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<link>.*?)"',re.S)


child_href_list=[]
res1 = obj1.finditer(resp.text)
for item in res1:
    ul = item.group('ul')
    # print(ul)

    # 提取子页面链接
    res2=obj2.finditer(ul)
    for itt in res2:
        # 拼接子页面的url地址 域名+子页面地址
        child_href = domain + itt.group('href').strip("/")
        child_href_list.append(child_href)
del(child_href_list[0])

f=open('dytt89.csv',mode="w",encoding="utf-8",newline='')
csvwriter = csv.writer(f)
#提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href,headers=headers,verify=False)
    child_resp.encoding = 'gb2312'
    res3 = obj3.search(child_resp.text)
    # print(res3.group('title'))
    # print(res3.group('link'))

    # 这种方式输出是下载链接换行
    # str1=res3.group('title')
    # str2=res3.group('link')
    # csvwriter.writerow(str1.split(),str2.split())
    # csvwriter.writerow(str2.split())

    #这种方式输出是保存成一个字典，名字和下载链接在一行 
    dic=res3.groupdict()
    csvwriter.writerow(dic.values())
    child_resp.close()
f.close()
resp.close()
print('保存完毕')
