import requests        # 인터넷 사이트 연결
from bs4 import BeautifulSoup

url = "http://www.naver.com"
response = requests.get(url)

soup = BeautifulSoup(response, "html5lib")

print(soup)
