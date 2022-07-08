from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

chrome_driver_path = "/Users/parinita/Development/chromedriver"
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")


class InstaFollower:
    def __init__(self,driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USER_NAME)
        time.sleep(3)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        time.sleep(3)

        password.send_keys(Keys.ENTER)

        self.driver.quit()

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()