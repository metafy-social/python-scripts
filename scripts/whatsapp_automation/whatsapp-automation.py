from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Scan the QR code and then press "enter"')
name_of_recipient = input('To whom do you want to send the message:')
msg = input('Enter your message:')

user = driver.find_element_by_xpath(f'//span[@title = "{name_of_recipient}"]')
user.click()
textbox = driver.find_element_by_class_name('_3uMse')

for i in range(200):
  textbox.send_keys(msg)
  send = driver.find_element_by_class_name('_1U1xa')
  send.click()
  time.sleep(5)

driver.quit()
