# 防盗链

# 1.拿到contId
# 2.拿到videoStatus返回的json. -> srcURL
# 3.srcURL里内容进行修正
# 4.下载视频
import requests
url = "https://www.pearvideo.com/video_1732516"
contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.33921492499284667"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    # 防盗链:溯源，当前本次请求的上一级是谁
    "Referer":url
}
resp = requests.get(videoStatusUrl,headers=headers)
print(resp.text)

resp.close()
