from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

consumer_token = os.getenv("TWITTER_CONSUMER_TOKEN")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
