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

- [WhatIsMyBrowser](https://www.whatismybrowser.com/detect/what-is-my-user-agent) 를 통해 User Agent 값 확인 가능
- User Agent 값을 통해 403 에러 접근 가능 -> 접속자 확인

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

## BeautifulSoup4

### 기본

- **lxml** 모듈을 사용하여 **requests** 를 통해 가져온 HTML 문서를 **BS4 객체**로 변환
- 변환된 BS4 객체를 통해 HTML의 Element로 접근
- get_text() : text 가져오기
- HTML 구조상 형제 관계
  - next_sibiling(),next_siblings(), find_next_sibling('key'), find_next_sibilings('key') ... ,(previous 도 있다)
- HTML 구조상 부모 관계

  - parent()

            import requests
            from bs4 import BeautifulSoup

            url = "https://comic.naver.com/webtoon/weekday.nhn"
            res = requests.get(url)
            res.raise_for_status()

            # requests를 통해 가져온 html 문서를 lxml 파서를 통해 BS 객체로 변환

            soup = BeautifulSoup(res.text, 'lxml')

            # 만들어진 soup을 통해 html의 element에 접근할 수 있다

            #print(soup.title)
            #print(soup.title.get_text())
            print(soup.a) # 첫번쨰로 발견되는 a element 정보가 출력
            print(soup.a.attrs, end='\n\n') # dict 형태로 a의 속성들만 출력
            print(soup.a['href']) # a 속성 dict 중 key값이 'href'인 value 출력

            # 태그가 a 에서 class = Nbtn_upload 인 element 출력

            find = soup.find('a', attrs={'class':'Nbtn_upload'})
            print(find, end='\n\n')

            rank1 = soup.find("li",attrs={'class':'rank01'})
            print(rank1.a) # soup을 통해서 발견한 rank1 객체에서 a element 정보만 출력
            print(rank1.a.get_text())

            #html 구조상 형제 관게
            rank2 = rank1.next_sibling.next_sibling
            rank3 = rank2.next_sibling.next_sibling

            print('rank2:',rank2.a.get_text())
            print('rank3:',rank3.a.get_text())

            rank2 = rank3.previous_sibling.previous_sibling
            print('rank2:',rank2.a.get_text())

            #HTML 구조에서 부모관계
            print(rank1.parent)

            rank2 = rank1.find_next_sibling('li') # li 태그를 가진 다음 형제 찾기
            rank2 = rank3.find_previous_sibling('li')
            print('rank2:', rank2.a.get_text())
            print('rank3:',rank3.a.get_text())

            # 이어지는 모든 형제의 값 찾기

            print(rank1.find_next_siblings('li'))

            #text 기반 찾기 -> a element 중 text = '고수-2부 111화'
            webtoon = soup.find('a', text = '고수-2부 111화')
            print(webtoon)

### 활용

- 링크 가져오기
- 페이지 넘어가기

  - 페이지는 url 상의 page 값을 format과 for 구문을 통해 변경할 수 있다.

  #노트북 정보 찾기
  import requests
  import re
  from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

# 1~5 페이지 정보 가져오기

for i in range(1, 6):

    print('페이지:',i)
    #url 내 페이지 값을 format을 통해 변경
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)

    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # search-product로 시작하는 class 중 li의 element 반환
    items = soup.find_all('li', attrs = {'class':re.compile('^search-product')})
    print(items[0].find('div',attrs = {'class':'name'}).get_text())


    for item in items:

        #광고 제품 제외
        ad_badge = item.find('span', attrs = {'class':'ad-badge-text'})
        if ad_badge:
            print('---------------------------------')
            print('해당 상품은 광고 제품이므로 제외합니다')
            print('---------------------------------')
            continue

        # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회

        name = item.find('div',attrs = {'class':'name'}).get_text() # 제품명

        price = item.find('strong', attrs = {'class':'price-value'}).get_text() # 가격

        rate =item.find('em',attrs = {'class':'rating'}) # 평점

        if rate:
            rate = rate.get_text()
        else:   # 평점이 없는 상품의 경우
            print('---------------------------------')
            print('평점 없는 제품 제외합니다')
            print('---------------------------------')
            continue

        rate_cnt = item.find('span',attrs = {'class':'rating-total-count'}) # 평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
        else:   # 평점 수가 없는 상품의 경우
            print('---------------------------------')
            print('평가 참여 저조 제품 제외합니다')
            print('---------------------------------')
            continue

        #애플 제품 제외
        if 'Apple' in name:
            print('---------------------------------')
            print('애플 제품 제외합니다')
            print('---------------------------------')
            continue

        link = item.find('a', attrs = {'class':'search-product-link'})['href']

        if float(rate) >= 4.5 and int(rate_cnt[1:-1]) >= 50:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"제품명 : {rate}점 {rate_cnt} 개")
            print('바로가기: {}'.format('https://www.coupang.com' + link))
