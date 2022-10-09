

import requests
from bs4 import BeautifulSoup
import urllib.request
from email_scraper import scrape_emails
import pandas as pd
from google.colab import files
 

urlid = input("Enter Website url (i.e.: example.com): ")
url = "https://"+urlid+"/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
response = []
email = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))
for i in range(len(urls)):
  if(urls[i].startswith("https://")):
    fp = urllib.request.urlopen(url+urls[i])
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    response.append(scrape_emails(mystr))
  else:
    fp = urllib.request.urlopen(url+urls[i])
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    response.append(scrape_emails(mystr))

for r in range(len(response)):
  if not response[r]:
    continue
  else:
    email.append(response[r])

df = pd.DataFrame(email, columns=["Email"])
df.to_csv('email.csv', index=False)

files.download("email.csv")

