import re

# # findall: 匹配字符串中所有符合正则的内容
# lst=re.findall(r"\d+","我的电话号是：10086")
# print(lst)

# # finditer匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容要.group()
# it=re.finditer(r"\d+","我的电话号是：10086,我女朋友的是：10000")
# for i in it:
#     print(i.group())

# # search()找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
# s=re.search(r"\d+","我的电话号是：10086,我女朋友的是：10000")
# print(s.group())

# # match从头开始匹配
# s=re.match(r"\d+","10086,我女朋友的是：10000")
# print(s.group())

# # 预加载正则表达式
# obj = re.compile(r"\d+")
# res=obj.finditer("我的电话号是：10086,我女朋友的是：10000")
# print(res)

# (?P<分组名字>正则)    可以单独从正则匹配的内容中进一步提取内容
s="""
<div class='qw'><span id='1'>过亲临</span></div>
<div class='as'><span id='2'>宋轶</span></div>
<div class='jj'><span id='3'>大聪明</span></div>
<div class='gf'><span id='4'>范思哲</span></div>
"""

obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>",re.S)  #re.S是可以匹配换行符
res = obj.finditer(s)
for i in res:
    print(i.group("wahaha"))
    print(i.group("id"))