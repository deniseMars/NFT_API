import requests
import pandas as pd
import tweepy
import configparser
# read credentials from config
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['API_Key']
api_key_secret = config['twitter']['API_Key_Secret']
access_token = config['twitter']['Access_Token']
access_token_secret = config['twitter']['Access_Token_Secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Exercise: Get my public tweets

# Set data in table
columnns = ['Time', 'User', 'Tweet', 'location']
data = []

# Define timeframe
start_date='2022-01-01'
end_date='2022-05-01'

query = ['nft', 'nftart']
response = api.search_tweets(q=query, count=3000)
for tweet in response:
    data.append([tweet.created_at, tweet.user.name, tweet.text,tweet.user.location])
df = pd.DataFrame(data, columns=columnns)
print(df)
# Cambiare nome file
df.to_csv('nft_tweets1.csv')