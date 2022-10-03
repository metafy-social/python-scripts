import pdfplumber
import pandas as pd
from google.colab import drive
import os
drive.mount('/content/gdrive')
os.chdir("/content/gdrive/PATH TO FOLDER CONTAINING INVOICES PDF")
os.getcwd()
invoices = os.listdir()
print(invoices)
import re
df = []
for inv in invoices:
  gst = pdfplumber.open(inv) #it will open each file in the directory
  page = gst.pages[0] #selecting the first page
  text = page.extract_text()
  gst_no = re.compile(r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}')
  m =gst_no.findall(text)
  print(m)
  df = df+[m]
gstin = pd.DataFrame(df)
gstin
gstin.to_csv('gstin.csv', index=False)