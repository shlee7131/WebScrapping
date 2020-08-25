import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')


# soup 객체에서 태그명이 a 이고 class = title 인 정보 가져오기
cartoons = soup.find_all('td', attrs = {'class':'title'})

# 마음의 소리 목록 가져오기
for cartoon in cartoons:
    print(cartoon.get_text())

title = cartoons[0].a.get_text()
link = cartoons[0].a['href']
print(title)
print('https://comic.naver.com'+link)


for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title, link)


# 평점 구하기
rates = soup.find_all('div', attrs = {'class':'rating_type'})
for rate in rates:
    print(rate.find('strong').get_text())

# 최근 만화 10개 평균 구하기
total_rates = 0
for rate in rates:
    score = float(rate.find('strong').get_text())
    total_rates += score

print('전체 점수 : {0:.3}'.format(total_rates))
print('평균 점수 : {0:.3}'.format(total_rates / len(rates)))






