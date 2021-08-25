# 安装
# pip install bs4 -i 清华源

# 拿到页面源码
# 使用bs4进行解析，拿到数据

from os import close
import requests
from bs4 import BeautifulSoup 
import csv

url="http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)


f=open('caijia.csv',mode="w",encoding="utf-8",newline='' )
csvwriter = csv.writer(f)
# 解析数据
# 1.把页面源码给bs4处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser") #可以加一个html.parser指定html解析器

# 2.从bs对象中查找数据
# find(标签,属性)
# find_adl
# table=page.find("table",class_="hq_table")  #class是python关键字所以改成class_
table = page.find("table",attrs={"class":"hq_table"}) #和上一行作用一样
print(table)

# 拿到所有数据行，第一行是表头所以从第二行开始
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td") #拿到每行中所有的td
    name = tds[0].text  #
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    data = tds[6].text
    csvwriter.writerow([name,low,avg,high,gui,kind,data])

f.close()
resp.close()
print('over')