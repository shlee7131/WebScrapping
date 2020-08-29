import requests
from bs4 import BeautifulSoup


url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Accept-Language": "ko-KR,ko"  # 한글 페이지 반환, 한글 페이지가 없으면 기본 페이지 반환
}


res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
print(len(movies))  # 동적 웹페이지여서 모든 정보가 한번에 오지 않는다


with open("moive.html", "w", encoding='utf8') as f:
    # f.write(res.text)
    f.write(soup.prettify())  # html 파일을 예쁘게 출력


for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    print(title)
