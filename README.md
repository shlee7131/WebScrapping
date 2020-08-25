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

## Regular Expression

- p = re.compile("원하는 형태")
- match : 주어진 문자열의 처음부터 일치하는지 확인
- search : 주어진 문자열 중에 일치하는게 있는지 확인
- findall : 일치하는 모든 것을 리스트 형태로 반환
- . (ca.e): 하나의 문자 -> care, cafe, case (O) | caffe(X)
- ^ (^de) : 문자열의 시작 -> desk, destination (0) | fade (X)
- $ (se$) : 문자열의 끝 -> case, base (0) | face (X)

        #정규식 표현
        import re

        # ca?e 로 표현된 문자를 찾아내기

        p = re.compile("ca.e") # p = re.compile("원하는 형태")

        # . (ca.e): 하나의 문자 -> care, cafe, case (O) | caffe(X)

        # ^ (^de) : 문자열의 시작 -> desk, destination (0) | fade (X)

        # $ (se$) : 문자열의 끝 -> case, base (0) | face (X)

        m = p.match("case") # 비교하려는 값 전달
        print(m.group()) # 매치되지 않으면 에러가 발생

        def print_match(m):
        if m:
        print("m.group():" , m.group()) # 표현식과 일치하는 문자열 반환
        print("m.string:" ,m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작과 끝 index
        else:
        print("매칭되지 않음")

        m = p.match("coffe")
        print_match(m) # 매칭되지 않음

        m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
        print_match(m) # careless가 아닌 care 만 출력

        m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
        print_match(m)

        lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 반환
        print(lst)
        lst = p.findall("good care cafe")
        print(lst)

## User Agent
