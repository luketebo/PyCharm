import requests

url = "https://www.wjx.cn/vm/tXzB5r4.aspx"

headers = {
    "Accept": "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)",
    "X-Amzn-Trace-Id": "Root=1-628b672d-4d6de7f34d15a77960784504"}

response = requests.get(url, headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(response.text)
