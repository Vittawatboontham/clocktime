#CLOCK IN 
from typing import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 
import requests
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

user = "Vittawatboo"
pwd = "Aqzaqaqzaq2"

#line config
url = 'https://notify-api.line.me/api/notify'
token = '4JkYW52CLIFir8wbmfQOSDivK8mFj2xjmh0fx3mLdKV'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

def clocktime(user,passs):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.delete_all_cookies()
    time.sleep(5)
    driver.get("https://callservice.gosoft.co.th/WebReport")
    time.sleep(1)
    username = driver.find_element_by_xpath('//*[@id="j_username"]')
    username.send_keys(user)

    password = driver.find_element_by_xpath('//*[@id="j_password"]')
    password.send_keys(passs)

    dropdown = Select(driver.find_element_by_id('companyDropdown'))

    dropdown.select_by_value('โกซอฟท์ (ประเทศไทย) จำกัด')

    clicklogin = driver.find_element_by_xpath('//*[@id="modal-dialog-control"]/div/div[2]/div[4]/input')
    clicklogin.click()
    time.sleep(1)
    toclock = driver.find_element_by_xpath('//*[@id="navbar"]/ul[1]/li[2]/a')
    toclock.click()
    time.sleep(1)
    clockin = driver.find_element_by_xpath('//*[@id="clockingButton"]')
    clockin.click()
    time.sleep(5)
    driver.close()

try:
    clocktime(user,pwd)
    msg = 'Clock in Success นอนต่อได้',current_time
   
except Exception as e: 
    msg = 'Clock in FAIL ไปแต้บบัตรเร็ว',current_time,' Python error :: ',e

finally :
    r = requests.post(url, headers=headers, data = {'message':msg})