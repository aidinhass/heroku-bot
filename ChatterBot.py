# Dependencies
import tweepy
import json
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys
consumer_key = "pWaFRDgs0S7kyzHX9ZLfNwxhX"
consumer_secret = "iAcooaCTfBUi9HpZM2ZpDAwKyNdRnQX3Ed9nOcb4mWJELgqlGH"
access_token = "777278389-wVm7P0RGRNr4YHVW85zXz8u4ngMs3EBaiKijmdBV"
access_token_secret = "y1o6ddNxbJfHz2h3mOux10LKDbLbFAvQ0VBTy4Fovp4Hs"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets

quote_list = [
    "Quote 11",
    "Quote 21",
    "Quote 31"]

# Create function for tweeting
def QuoteItUp(quote_num):

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully!")

# Set timer to run every minute
counter = 0

while(counter < len(quote_list)):
    QuoteItUp(counter)
    time.sleep(60)
    counter += 1

