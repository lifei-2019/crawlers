import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.net/p/gaoqing/cn/"
resp = requests.get(url)
resp.encoding = 'utf-8'

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
resp.close()


for a in alist:
    href=a.get('href')
    children_page_resp = requests.get(url+href.strip('p/gaoqing/cn/'))
    children_page_resp.encoding = 'utf-8'
    child_page_text = children_page_resp.text
    # print(children_page_resp)
    # 从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    div = child_page.find('div',attrs={'class':'ImageBody'})
    img = div.find("img")
    src = img.get("src")
    children_page_resp.close()
    # 下载图片
    img_resp=requests.get(src)
    # img_resp.content 这里拿到的是字节
    img_name = src.split("/")[-1] #拿到url中的最后一个/以后的内容

    with open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)
    print("over", img_name)
    img_resp.close()
    time.sleep(1)
print('all over')

