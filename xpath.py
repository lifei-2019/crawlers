# xpath是在xml文档中搜索内容的一门语言
# html是xml的一个子集
# pip install lxml
# 此时遇到一个问题安装完成后仍然报无法引用Import “xxx“ could not be resolved from source
# 需要再vscode里的settings里设置python path

import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
# 解析
html = etree.HTML(resp.text)
# 拿到每一个服务商的div，这一部要右键copy源码中的xpath
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:  #每一个服务商信息
    price=div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title="saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()"))
    con_name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
    print(price)

resp.close()