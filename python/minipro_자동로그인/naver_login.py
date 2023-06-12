from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
import pyperclip


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()
warnings.filterwarnings('ignore')

# 1)
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
driver.get(url)
time.sleep(5)
