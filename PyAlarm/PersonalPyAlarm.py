import time
import re
import smtplib
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#Set Options
options = webdriver.ChromeOptions()
#options.add_argument("headless")

#Set Wake Options
print("Wake Me Up! \n Script By: Nirinium of NTG|RF \n")
phoneNum = input("Enter Phone #:")
hour = "6" #id = localHour
minute = "0" #id = localMinu
ampm = "a" #id = localAmpm

#Defines
slp = time.sleep(1)

#Webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
driver.get("http://www.wakeupdialer.com")
assert "WakeUpDialer.com" in driver.title

#Find Elements
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

#Get Result & Print & Mail
scr = driver.get_screenshot_as_file("scr.png")

cap = "scr.png"
img_data = open(cap, 'rb').read()

me = "bot@nirinium.com"
you = "wills.colton@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alarm Set!"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
    <head></head>
    <body>
    <p>Alarm Set!<br>
        How are you?<br>
        Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    </body>
</html>
"""
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
image = MIMEImage(cap, 'png')
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
msg.attach(image)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('wills.colton', 'bmlyaW5pdW0=')
mail.sendmail(me, you, msg.as_string())
mail.quit()

#Send

#finally, but sleep first for debug
print("Script complete.")
time.sleep(1000)
driver.close()

