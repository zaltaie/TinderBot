'''
This will scrape data from Tinder for all data, whenever they are found,
it will be exported into a CSV files.
'''

#------------------------------------------------------------------

from selenium import webdriver
import sys
from login import user, passw
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv

#------------------------------------------------------------------

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    # ------------------------------------------------------------------
    # Log's in to Tinder.com
    # ------------------------------------------------------------------


    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        try:
            string = "//button[contains(.,'More Options')]"
            moreops = self.driver.find_element_by_xpath(string)
            moreops.click()
            sleep(1)
            fb_path = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button'
            fb_btn = self.driver.find_element_by_xpath(fb_path)
            fb_btn.click()
        except:
            fb_path = '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button'
            fb_btn = self.driver.find_element_by_xpath(fb_path)
            fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]
        self.driver.switch_to.window(popup)

        sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(user)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(passw)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2)
        # switch to original window

        self.driver.switch_to.window(base_window)

        sleep(3)

        '''
        #------------------------------------------------------------------
        #Optional phone login

        phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        phone_in.send_keys(phone_num)

        continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        continue_btn.click()

        #Need to input authentication code manually
        sleep(15)
        #------------------------------------------------------------------
        '''


        loc_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_popup.click()

        notif_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notif_popup.click()

        sleep(8)

        '''
        #------------------------------------------------------------------
        #Optional passport popup dismiss

        passport_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        passport_popup.click()
        #------------------------------------------------------------------
        '''
