import pyshorteners
import argparse

def generateShortURL(URL):
   shortener = pyshorteners.Shortener()
   url = URL
   shorten_url=  shortener.tinyurl.short(url)
   print("Shorten URL is: " + shorten_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("URL",type = str)

    args = parser.parse_args()
    generateShortURL(args.URL)

#Using bitly_api
"""
import bitly_api
import argparse

def generateShortURL(url):
  access_token_ID = "" #ACCESS ID GENERATED FROM WEBSITE

  connection = bitly_api.Connection(access_token= access_token_ID)
  shorten_url = connection.shorten(url)
  print("Shorten URL is: "shorten_url.get('url'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("URL",type = str)

    args = parser.parse_args()
    generateShortURL(args.URL)
"""