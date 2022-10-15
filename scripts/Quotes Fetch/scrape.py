#import section
import requests
from bs4 import BeautifulSoup as bs
import argparse
from random import choice

# parser object to read cli content
parser = argparse.ArgumentParser()
parser.add_argument("-q", help="for search term")
parser.add_argument("-r", help="if you want one random quote")

args = parser.parse_args()


search_term = args.q
page = 1
# URl definition
url = f"https://www.brainyquote.com/search_results?q={search_term}&pg={page}"

# main program
r = requests.get(url)
soup = bs(r.content, "html.parser")
anchor1 = soup.find_all('a', {"class": "b-qt"})
anchor2 = soup.find_all('a', {"class": "bq-aut"})


if args.r != None:
    quote = choice(
        [f"{quote.text.strip()} - {author.text.strip()}" for quote, author in zip(anchor1, anchor2)])
    print(quote)
else:
    for i, (quote, author) in enumerate(zip(anchor1, anchor2)):
        quote = quote.find('div').text.strip()
        author = author.text.strip()
        print(f"[{i}] : {quote} - {author}")
