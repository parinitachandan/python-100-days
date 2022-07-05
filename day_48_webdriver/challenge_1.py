from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/parinita/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for event in range(len(event_time)):
    events[event] = {
        "time": event_time[event].text,
        "name": event_name[event].text
    }

print(events)
driver.quit()