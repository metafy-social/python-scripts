import requests
import smtplib
from email.message import EmailMessage

MY_EMAIL = ""
MY_PASSWORD = ""

recipients = []

em = EmailMessage()
em['From'] = MY_EMAIL

STOCK_LIST = {"TSLA": "Tesla Inc.",
              "AAPL": "Apple Inc.",
              "FB": "Meta Platforms, Inc.",
              "GOOG": "Alphabet Inc.",
              "NFLX": "Netflix, Inc",
              }

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

message = "\n"

for key in STOCK_LIST:
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": key,
        "apikey": STOCK_API_KEY,
    }
    COMPANY_NAME = STOCK_LIST[key]

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    yesterday_closing_price = yesterday_data["4. close"]
    day_before_yesterday_data = data_list[1]
    day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
    difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
    if difference > 0:
        notation = "🔺"
        updown = "up"
    else:
        notation = "🔻"
        updown = "down"

    difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
    diff_percent = round(((difference / float(yesterday_closing_price)) * 100), 2)

    if diff_percent > 0.05:
        news_params = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        articles = news_response.json()["articles"]
        article = articles[0]

        message = message + f"{COMPANY_NAME}({key}): {notation}{diff_percent}%\nHeadlines: {article['title']}. \nBrief: {article['description']}\n\n"


print(message)
with smtplib.SMTP("smtp.gmail.com", port=587) as server:
    server.starttls()
    server.login(user=MY_EMAIL, password=MY_PASSWORD)
    em["Subject"] = "Your daily watchlist 📈"
    for recipient in recipients:
        em.set_content(message)
        em['To'] = recipient
        server.send_message(em)
        del em["To"]



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
