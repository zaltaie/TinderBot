from selenium import webdriver
import sys
sys.path.insert(1,'/Users/zaid/Downloads')
from login import user, passw
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/zaid/Downloads/chromedriver')

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        try:
            string = "//button[contains(.,'More Options')]"
            moreops = self.driver.find_element_by_xpath(string)
            moreops.click()
            sleep(0.25)
            fb_path = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button'
            fb_btn = self.driver.find_element_by_xpath(fb_path)
            fb_btn.click()
        except:
            fb_path = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button'
            fb_btn = self.driver.find_element_by_xpath(fb_path)
            fb_btn.click()
