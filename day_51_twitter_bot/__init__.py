from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement

o = webdriver.ChromeOptions()
o.add_argument("--user-data-dir=/Users/parinita/Library/Application Support/Google/Chrome/");

o.add_argument("--profile-directory=Profile 2");
o.add_argument('--no-sandbox')
chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://twitter.com/i/flow/login")

time.sleep(15)

google_login_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]')

google_login_button.click()

