import time
import requests # Will help us to get out url directed
from bs4 import BeautifulSoup # Will help us to scrap us the data

import os
import smtplib # this module is used for sending mail
from email.message import EmailMessage

email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")

# I have used this since I have hidden my credentials

URL = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_3?crid=3BF9J6OT56GW0&keywords=macbook+m1&qid=1665331351&qu=eyJxc2MiOiIzLjgzIiwicXNhIjoiMi43NiIsInFzcCI6IjEuNTIifQ%3D%3D&sprefix=macbook+m1%2Caps%2C3675&sr=8-3"

def check_price():
    #Copy url of the product that you are looking for
    headers = {"user-Agents" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    # Now lets print our product title to veerify that its working
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_ = "a-size-large product-title-word-break").get_text()
    price = soup.find(class_ = "a-price-whole").get_text()
    converted_price = price[:6].replace(",","") # We don't want comma so we replaced with ""

    print(title.strip())
    print(converted_price)

    # Now we will send mail if the converted price is less than present price

    if(converted_price < 92890):
        send_mail()

def send_mail():
    message = EmailMessage()
    message['Subject'] = "Your favourite product is now at cheaper price!!😍"
    message['From'] = email_id
    message['to'] = "mobir99513@lutota.com" #Any random email you can give whom you want to send the email
    message.set_content("Hey check this amazon link : https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_3?crid=3BF9J6OT56GW0&keywords=macbook+m1&qid=1665331351&qu=eyJxc2MiOiIzLjgzIiwicXNhIjoiMi43NiIsInFzcCI6IjEuNTIifQ%3D%3D&sprefix=macbook+m1%2Caps%2C3675&sr=8-3")


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:   #465 is the port number
         smtp.login(email_id, email_pass)
         smtp.send_message(message)

while True:
    check_price()
    time.sleep(10)