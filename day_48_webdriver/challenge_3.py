from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Hello")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Hi")

email = driver.find_element(By.NAME, "email")
email.send_keys("hello@hi.com")

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.send_keys(Keys.ENTER)  # or submit.click()

driver.quit()
