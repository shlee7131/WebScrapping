#정규식 표현
import re

# ca?e 로 표현된 문자를 찾아내기
p = re.compile("ca.e") # p = re.compile("원하는 형태")

# . (ca.e): 하나의 문자 -> care, cafe, case (O) | caffe(X)
# ^ (^de) : 문자열의 시작 -> desk, destination (0) | fade (X)
# $ (se$) : 문자열의 끝 -> case, base (0) | face (X)

m = p.match("case") # 비교하려는 값 전달
print(m.group()) #  매치되지 않으면 에러가 발생




def print_match(m):
    if m:
        print("m.group():" , m.group())  # 표현식과 일치하는 문자열 반환 
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


# p = re.compile("원하는 형태")
# match : 주어진 문자열의 처음부터 일치하는지 확인
# search : 주어진 문자열 중에 일치하는게 있는지 확인
# findall : 일치하는 모든 것을 리스트 형태로 반환


# . (ca.e): 하나의 문자 -> care, cafe, case (O) | caffe(X)
# ^ (^de) : 문자열의 시작 -> desk, destination (0) | fade (X)
# $ (se$) : 문자열의 끝 -> case, base (0) | face (X)
