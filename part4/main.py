import requests as api
import datetime
import os
from twilio.rest import Client
#from twilio.http.http_client import twilioHttpClient

STOCK_NAME = "TSLA"#"AMZN"
COMPANY_NAME = "Tesla Inc"#"Amazon Inc"#

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_ALPHA_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
API_NEWS_KEY = os.environ.get("NEWS_API_KEY")

account_sid = os.environ["TWILIO_ACCOUNT_SID"] = "AC51549b8c1bb41e31f4e02739f8693d8e"
auth_token = os.environ["TWILIO_AUTH_TOKEN"] = "abdc728a9eb2df7d773bcd89b727a0ff"
phone_number = '+14143166728'

stock_params = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": API_ALPHA_KEY
  }

def main():

        ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    #TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
  response = api.get(STOCK_ENDPOINT, params = stock_params)
  data = response.json()["Time Series (Daily)"]
  data_list = [value for (key, value) in data.items()]
  yesterday_closing_price = data_list[0]["4. close"] # from data list yesterday data -> data_list[0]
  print(yesterday_closing_price)
  
    #TODO 2. - Get the day before yesterday's closing stock price
  day_before_yesterday_data = data_list[1]["4. close"]
  print(day_before_yesterday_data)
    #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
  difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data))
  print(difference)
    #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
  percentage_difference = (difference / float(day_before_yesterday_data)) * 100
  print(f"{percentage_difference} %")
    #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
  if percentage_difference > 1:
    news_params = {
      "apiKey": API_NEWS_KEY,
      "qInTitle": COMPANY_NAME,
      "language": "en"
    }
        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # Hint: https://newsapi.org/docs/endpoints/everything
    news_response = api.get(NEWS_ENDPOINT, params=news_params)
    news_articles_data = news_response.json()["articles"]
    print(news_articles_data)
    print(len(news_articles_data))
    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = news_articles_data[:3]
    print(three_articles)

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    #TODO 9. - Send each article as a separate message via Twilio.



    #Optional TODO: Format the message like this:
  """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

