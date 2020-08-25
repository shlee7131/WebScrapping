import requests

# 403 오류가 나는 url -> 사람이 아닌 기계의 접속으로 판단
url = "https://arch-it.tistory.com/"

#User-Agent 값을 활용하여 기계가 아닌 사람의 접속 확인
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get(url, headers = headers) #문제 없이 처리

res.raise_for_status()

# 접속은 오류라도 html 정보는 가져올 수 있다
with open("Arch-IT Tistory.html", "w", encoding="utf8") as f:
    f.write(res.text)



