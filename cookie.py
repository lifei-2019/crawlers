# 进阶概述
import requests

# session是一连串请求
# 会话
session = requests.session()

# 1.登录
url="https://passport.17k.com/ck/user/login"
data = {
    "loginName": "18614075987",
    "password": "q6035945"
}
session.post(url, data=data)
# resp.encoding = 'utf-8'
# print(resp.text)
# print(resp.cookies)

# 2.拿数据
resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
resp.encoding = 'utf-8'
print(resp.json())


# 还有一种方法
# resp=requests.get("链接", headers={
#     "Cookie":"啥啥啥"
# })

resp.close()