import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

url = str(input("url: "))
interval = int(input("interval(s): "))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

PrevVersion = ""
FirstRun = True
while True:    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup(["script", "style"]):
        script.extract()
    soup = soup.get_text()
    
    if PrevVersion != soup:
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            print("Started Monitoring " + url + " " + str(datetime.now()))
        else:
            print("Changes detected at: " + str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            d = difflib.Differ()
            diff = d.compare(OldPage, NewPage)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            #print(out_text)
            OldPage = NewPage
            # print ('\n'.join(diff))
            PrevVersion = soup
    else:
        print("No Changes Detected " + str(datetime.now()))
    time.sleep(interval)
    continue
