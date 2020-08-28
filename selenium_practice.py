from selenium.webdriver.common.keys import Keys  # 엔터키 입력을 위해
from selenium import webdriver as wd

# chromedriver의 디렉토리 정보를 괄호에 넣어주어야 한다
browser = wd.Chrome()  # "./chromedriver.exe" , 같은 경로에 있으면 생략 가능
browser.get('http://naver.com')

# 로그인 버튼
elem = browser.find_element_by_class_name('link_login')

# 로그인 버튼 클릭
elem.click()

browser.back()
browser.forward()
browser.back()
browser.refresh()

# 검색창
elem = browser.find_element_by_id("query")

# 글자를 입력하는 방법
elem.send_keys("글자 입력 완료")
# 엔터키 입력
elem.send_keys(Keys.ENTER)

# a 태그에 해당하는 객체 전부 탐색
elem = browser.find_elements_by_tag_name("a")

for e in elem:
    e.get_attribute("href")

browser.get('http://daum.net')

elem = browser.find_element_by_name("q")
elem.send_keys("글자 입력 완료")

# 검색 버튼 Xpath
elem = browser.find_element_by_xpath(
    "//*[@id=\"daumSearch\"]/fieldset/div/div/button[2]")
# elem 클릭
elem.click()

# 브라우저 탭종료
browser.close()

# 브라우저 전체 종료
browser.quit()
