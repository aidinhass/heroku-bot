# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "CrcG6uQ3dbkxm5YBXFaB7fEzr"
consumer_secret = "khXxwvCxvHv99b7LBY5DMZbMTaIx6IjONzqpIwedoc85zgBmrQ"
access_token = "998708479354392577-v7ue24YeFRCyNXfEGM30tyIW50bAi1m"
access_token_secret = "196hEBE1DczjXCUNhZ6KFZxYfQDvEKduE4rpgF1cUwaMi"

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

