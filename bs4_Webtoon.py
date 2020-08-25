import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

## 네이버 웹툰 전체 목록 가져오기

cartoons = soup.find_all('a', attrs = {'class':'title'})
# soup 객체에서 태그명이 a 이고 class = title 인 정보 가져오기

for cartoon in cartoons:
    print(cartoon.get_text())




