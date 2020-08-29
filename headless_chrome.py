from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time


# selenium에서 브라우저를 띄우지 않고 수행
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size = 3840x2160")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2


# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기(2초씩 대기)
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all(
    "div", attrs={"class": "Vpfmgd"})  # 두가지 class 명 서치
print(len(movies))  # 동적 웹페이지여서 모든 정보가 한번에 오지 않는다

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "  <할인되지 않은 영화 제외>")
        continue

    # 할인 된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]

    print(f"제몱 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()
