import requests
from twilio.rest import Client
import os

# Stock API info.
STOCK = "TSLA"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your_stock_api_key"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# News API info.
COMPANY_NAME = "Tesla Inc"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your_news_api_key"
NEWS_PARAMETERS = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

# Twilio info.
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(STOCK_API_ENDPOINT, params=STOCK_PARAMETERS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

previous_day = float(stock_data_list[0]["4. close"])
two_days_ago = float(stock_data_list[1]["4. close"])

percent_change_in_price = previous_day / two_days_ago * 100

if percent_change_in_price > 105:
    symbol = "🔺"
else:
    symbol = "🔻"

if percent_change_in_price < 95 or percent_change_in_price > 105:
    print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(NEWS_API_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"{STOCK}: {symbol}{percent_change_in_price}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
                        .create(
                             body=article,
                            # Default numbers from Twilio documentation. Adjust accordingly.
                             from_='+15017122661',
                             to='+15558675310'

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

