from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
PHONE = 123456789

chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()


time.sleep(5)


email_field = driver.find_element(By.ID, "username")
email_field.send_keys(LINKEDIN_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(LINKEDIN_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()


time.sleep(3)

phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()

time.sleep(3)

cross_button: WebElement = driver.find_element(By.CLASS_NAME, 'artdeco-button')
cross_button.click()

time.sleep(3)

discard_button: WebElement = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[2]')
discard_button.click()

time.sleep(3)

driver.quit()




