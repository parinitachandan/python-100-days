from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count_lang = driver.find_element(By.XPATH, '//*[@id="articlecount"]')
print(article_count_lang.text)


article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.quit()


