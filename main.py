from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
import time
import os

options = Options()
options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)
driver.get("https://monkeytype.com/")
driver.maximize_window()

actions = ActionChains(driver)
time.sleep(0.5)

driver.find_element("xpath", '/html/body/div[8]/div/div[2]/div[2]/div[2]/div[1]').click()
time.sleep(0.5)

starttime = time.time()

while True:
  word = driver.find_element(By.CSS_SELECTOR, "#words > div.word.active").text
  actions.send_keys(word + " ")
  actions.perform()
  if time.time() - starttime > 30:
    break

time.sleep(1)
wpm = driver.find_element("xpath", "/html/body/div[9]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]").text

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists("screenshots"):
  os.mkdir("screenshots")

driver.save_screenshot("screenshots/" + wpm + "_wpm.png")
