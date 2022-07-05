from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.amazon.in/dp/B09YD89LQN/ref=syn_sd")

currency = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(currency.text + price.text)

driver.quit()



