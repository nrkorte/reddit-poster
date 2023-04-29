#!/usr/bin/env python

import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains

class bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
        self.driver.set_window_position(1000, 0)
        self.driver.maximize_window()
    def start(self, user, passw):
        time.sleep(3)
        self.driver.get("www.reddit.com")
    
    def begin(self):
        print()

if __name__ == "__main__":
    bot = bot()
    bot.start()
    bot.begin()