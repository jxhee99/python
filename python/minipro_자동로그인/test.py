# 1) selenium 기본 설정
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

## 자동입력 방지 문자 알림창 방지를 위한 import
import time
import warnings
import pyperclip

chrome_options = Options()   # 브라우저 꺼짐 방지
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 에러 메세지 삭제

# 2) 크롬 드라이버 최신 버전 자동 설치 & 서비스 만들기
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
warnings.filterwarnings('ignore')

# driver.implicitly_wati(5)  # 사이트 로딩시간 기다림 - 5초
driver.maximize_window()   # 화면 최대화

# 3) 로그인 창
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
driver.get(url)
time.sleep(1)

user_id = "wngml2666"
user_pw = "cbfjtm9725@"

# 2) 아이디 입력
elem_id = driver.find_element(By.CSS_SELECTOR, '#id')
#id = driver.find_element_by_xpath('//*[@id="id"]')
elem_id.click()
pyperclip.copy(user_id)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 3) 비밀번호 입력
elem_pw = driver.find_element(By.CSS_SELECTOR, '#pw')
#pw = driver.find_element_by_xpath('//*[@id="pw"]')
elem_pw.click()
pyperclip.copy(user_pw)
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 4) 로그인 버튼 클릭
log_ENT = driver.find_element(By.CSS_SELECTOR, '#log\.login')
#log_ENT = driver.find_element_by_xpath('//*[@id="log.login"]')
log_ENT.click()

# 5) html 정보 출력
# print(driver.page_source)

# 6) 브라우저 종료
# driver.close()
# driver.quit()
