import time
from selenium import webdriver

browser = webdriver.Chrome()

# 1. 브라우저 이동하기
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디  및 비밀번호 입력
browser.find_element_by_id("id").send_keys("ID")
browser.find_element_by_id("pw").send_keys("PW")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 시간 갭을 주어서 충돌 방지
time.sleep(2)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("NEW_ID")

# 6. html 정보 출력 -> 스크래핑 연동 가능
print(browser.page_source)

# 7. 브라우저 종료
browser.close()  # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
