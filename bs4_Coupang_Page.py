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
        



