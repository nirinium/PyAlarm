import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Set Options
options = webdriver.ChromeOptions()
#options.add_argument("headless")
 # yeet
#Set Wake Options
print("Wake Me Up! \n Script By: Nirinium of NTG|RF \n")
phoneNum = input("Enter Phone #:")
hour = "6" #id = localHour
minute = "0" #id = localMinu
ampm = "a" #id = localAmpm

#Defines
slp = time.sleep(1)

driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
driver.get("http://www.wakeupdialer.com")
assert "WakeUpDialer.com" in driver.title

elem = driver.find_element_by_id("iRecipient") #Where Phone # Is Entered
elem.send_keys(phoneNum)
slp
elem = driver.find_element_by_id("localHour")
elem.send_keys(hour)
slp
elem = driver.find_element_by_id("localMinu")
elem.send_keys(minute)
slp
elem = driver.find_element_by_id("localAmpm")
elem.send_keys(ampm)
slp
elem = driver.find_element_by_id("btn")
elem.click()

#finally, but sleep first for debug
time.sleep(100)
driver.close()
