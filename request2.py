import requests

url ="https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的字符串")
dat ={
    "kw":s 
}

# 发送post请求
resp=requests.post(url,data=dat)
# 将服务器返回的内容直接处理成json() =>dict
print(resp.json())
resp.close()



# 另一种方法s
# resp.encoding=resp.apparent_encoding
# print(resp.apparent_encoding)
# # 直接resp.text会出现乱码
# print(resp.text.encode('utf-8').decode('unicode_escape'))
# resp.close()