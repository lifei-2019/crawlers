open()

# mac默认utf-8 
# win默认gbk所以要加上encoding="utf-8" 
open("xxx", mode="abc", encoding="utf-8")

# 请求头里常见的一些
# user-Agent:请求载体的身份标识(用啥发送的请求)
# Refer:防盗链（即这次请求从哪个页面来的）
# cookie:本地字符串数据信息（用户登录信息，反爬的token)

# 响应头中的一些
# cookie:本地字符串数据信息（用户登录信息，反爬的token)
# 各种奇怪的字符串(类似与加了salt后加密，这个salt要自己找)

# 安装requests
# pip install requests