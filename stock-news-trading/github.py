import requests
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={PRICE_API_KEY}'
# print(url)
r = requests.get(url)
data = r.json()
now = dt.datetime.today()
now = str(now).split()[0]
# print(now)


# This should be 1 day ago
one_day_ago = dt.datetime.today() - dt.timedelta(days=3)
one_day_ago = str(one_day_ago).split()[0]
# print(one_day_ago)

# This should be 2 days ago
two_days_ago = dt.datetime.today() - dt.timedelta(days=4)
two_days_ago = str(two_days_ago).split()[0]
# print(two_days_ago)

# print(data["Time Series (Daily)"])

# This is to get the closing price
one_day_ago_low = float(data["Time Series (Daily)"][one_day_ago]["4. close"])
two_days_ago_low = float(data["Time Series (Daily)"][two_days_ago]["4. close"])
# print(one_day_ago_low)
# print(two_days_ago_low)

change = (one_day_ago_low - two_days_ago_low) / two_days_ago_low * 100
if change > 5 or change < -5:
    # print("Get News")
    url = ('https://newsapi.org/v2/everything?'
           f'q={STOCK}&'
           f'from=2022-10-22&'
           'sortBy=popularity&'
           f'apiKey={NEWS_API_KEY}')

    # print(url)
    response = requests.get(url)
    news_info = response.json()
    # print(url)
    # print(news_info["articles"][:3])
    first_3_articles = news_info["articles"][:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    for article in first_3_articles:
        if change > 0:
            message_to_be_sent = f'TSLA: 🔺{change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}'
            # print(message_to_be_sent)
            api_key = os.environ.get("OWN_API_KEY")
            account_sid = "YOUR TWILIO ACCOUNT SID"
            # auth_token = os.environ.get("AUTH_TOKEN")
            auth_token = "YOUR TWILIO AUTH TOKEN"
            print(auth_token)
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message_to_be_sent,
                from_="your virtual twilio number",
                to="your own phone number verified with Twilio"
            )
            print(message.status)
        else:
            message_to_be_sent = f'TSLA: 🔻{change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}'
            # print(message_to_be_sent)
            api_key = os.environ.get("OWN_API_KEY")
            account_sid = "YOUR TWILIO ACCOUNT SID"
            # auth_token = os.environ.get("AUTH_TOKEN")
            auth_token = "YOUR TWILIO AUTH TOKEN"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message_to_be_sent,
                from_="your virtual twilio number",
                to="your own phone number verified with Twilio"
            )
            print(message.status)

else:
    # print("No News")
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    url = ('https://newsapi.org/v2/everything?'
           f'q={STOCK}&'
           f'from=2022-10-22&'
           'sortBy=popularity&'
           f'apiKey={NEWS_API_KEY}')

    # print(url)
    response = requests.get(url)
    news_info = response.json()
    # print(url)
    # print(news_info["articles"][:3])
    first_3_articles = news_info["articles"][:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    for article in first_3_articles:
        if change > 0:
            message_to_be_sent = f'TSLA: 🔺{change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}'
            # print(message_to_be_sent)
            api_key = os.environ.get("OWN_API_KEY")
            account_sid = "YOUR TWILIO ACCOUNT SID"
            # auth_token = os.environ.get("AUTH_TOKEN")
            auth_token = "YOUR TWILIO AUTH TOKEN"
            print(auth_token)
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message_to_be_sent,
                from_="your virtual twilio number",
                to="your own phone number verified with Twilio"
            )
            print(message.status)
        else:
            message_to_be_sent = f'TSLA: 🔻{change}%\nHeadline: {article["title"]}\nBrief: {article["description"]}'
            # print(message_to_be_sent)
            api_key = os.environ.get("OWN_API_KEY")
            account_sid = "YOUR TWILIO ACCOUNT SID"
            # auth_token = os.environ.get("AUTH_TOKEN")
            auth_token = "YOUR TWILIO AUTH TOKEN"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message_to_be_sent,
                from_="your virtual twilio number",
                to="your own phone number verified with Twilio"
            )
            print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
