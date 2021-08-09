import requests        # 인터넷 사이트 연결

url = "http://www.naver.com"
response = requests.get(url)


print(response.text)