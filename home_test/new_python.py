import requests
# r中存储了该次会话的所有信息 请求和响应内容
r = requests.get(url="http://qa.yansl.com:8080/prefrenceArea/listAll")
# 请求方法
method = r.request.method
print(method)
# url
url = r.request.url
print(url)
# 请求头
headers = r.request.headers
print(headers)
# 请求正文
body = r.request.body
print(body)
# 响应状态码
status_code = r.status_code
print(status_code)
# 响应头
headers = r.headers
print(headers)
# 响应正文
# 文本格式
text = r.text
print(text)
# 字典格式
d = r.json()
print(d)
# 二进制格式
content=r.content
print(content)