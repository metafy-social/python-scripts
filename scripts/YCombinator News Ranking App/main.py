from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles=[]
articles_span = soup.find_all(name="span", class_="titleline")
for item in articles_span:
    articles.append(item.find(name='a'))

article_texts = []
article_links = []


for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest = max(article_upvotes)
largest_index = article_upvotes.index(largest)

print("Highest Ranked news for today is :\n")
print(f"Upvotes: {largest}")
print(f"Article Heading: {article_texts[largest_index]}")
print(f"Article Link: {article_links[largest_index]}")
