import tweepy
import config

auth = tweepy.AppAuthHandler(config.consumer_token, config.consumer_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, id='readikommunal', tweet_mode='extended').items(10):
    print(tweet.full_text)
