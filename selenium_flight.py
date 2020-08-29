from selenium import webdriver
# 반응 로딩 대기할 수 있는 방법 By, WebDirverWait, expected_conditions 활용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 창 크기 최대화

url = "https://flight.naver.com/flights"
browser.get(url)  # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 30일, 다음달 2일
browser.find_elements_by_link_text("30")[0].click()  # [0] -> 이번달, [1] -> 다음달
browser.find_elements_by_link_text("2")[1].click()  # [0] -> 이번달, [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# browser 객체에서 최대 10초 동안 대기 -> 해당 조건에 만족하는 Elem가 나타날 때 까지 => 10초 초과해도 안나오면 Error
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 동작이 10초 안에 일어났다 -> 성공
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()
    # 동작 실패로 인한 종료
