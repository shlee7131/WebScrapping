import requests
res = requests.get('http://google.com')

# 200 이면 정상, 403 이면 비정상(HTML 문서 가져올 수 없다)
print("응답코드 :",res.status_code)

'''
if res.status_code == requests.codes.ok: #requests.codes.ok 는 200과 같다
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드", res.status_code, "]")
'''

res.raise_for_status() # 스크래핑에 오류가 생기면 실행 중단(get과 짝궁)
print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

# 가져온 페이지 정보 파일로 만들기
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
