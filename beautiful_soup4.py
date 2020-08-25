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
print(soup.a.attrs, end='\n\n') #  dict 형태로 a의 속성들만 출력
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
