import csv
import requests
from bs4 import BeautifulSoup

#페이지 유동적
url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='

filename = '시가총액1-200.csv'
# 엑셀에서 한글파일 깨질때 utf-8-sig 변환
f = open(filename, 'w', encoding = 'utf-8-sig', newline = '')
writer = csv.writer(f) # csv

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split('\t')
#['N','종목명','현재가', ..]
print(type(title))
writer.writerow(title)


for page in range(1, 5):
    res = requests.get(url + str(page)) #페이지 변환
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'lxml')

    # table 태그에서 class 명인 type_2인 표의 tbody 에서 정보를 가져온다
    data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')

    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue

        #strip()을 활용하여 불필요한 공백 제거
        data = [column.get_text().strip() for column in columns] 
        #list 구조를 행으로 변환
        writer.writerow(data) 
        
