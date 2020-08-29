from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=3840x2160")

# headless chrome이 없는 기본 user agent 값 명시
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# User-Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
# User-Agnet 값을 기존 chrome의 user-agent값으로 명시하지 않는 경우 headless chrome 유저 추가되어 출력
print(detected_value.text)
browser.quit()
