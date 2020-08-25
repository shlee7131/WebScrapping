# WebScrapping

## X-Path

HTML구조에서 특정 부분의 위치를 빠르게 찾을 수 있도록 도와줌.

	<students>
		<student stn = "202001" >
			<name>철수</name>
			<major>소프트웨어</major>
		</student>
	<students>

위와 같은 경우, stn의 속성값을 통해 빠르게 접근할 수 있다.
- student/@202001

## Requests

    import requests

    res = requests.get('http://google.com')

    # 200 이면 정상, 403 이면 비정상(HTML 문서 가져올 수 없다)
    print("응답코드 :",res.status_code)


    ''' 세부적으로 아래와 같이 정상 및 비정상 실행에 대한 표기 가능
    if res.status_code == requests.codes.ok: #requests.codes.ok 는 200과 같다
    	print("정상입니다")
    else:
    	print("문제가 생겼습니다. [에러코드", res.status_code, "]")
    '''

    # 스크래핑에 오류가 생기면 실행 중단(위의 과정 대신에 간단하게 사용 - 주로 사용)
    res.raise_for_status()
    print("웹 스크래핑을 진행합니다")

    print(len(res.text))
    print(res.text)

    # 가져온 페이지 정보 파일로 만들기
    with open("mygoogle.html", "w", encoding="utf8") as f:
    	f.write(res.text)
