import tweepy
from decouple import config

# Add your keys and tokens here
API_KEY = config("OLD_API_KEY")
API_SECRET = config("OLD_API_SECRET")
ACCESS_TOKEN = config("OLD_ACCESS_TOKEN")
ACCESS_SECRET = config("OLD_ACCESS_SECRET")

# Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Test connection
try:
    user = api.verify_credentials()
    print(f"Authentication successful! Logged in as: {user.screen_name}")
except Exception as e:
    print(f"Error: {e}")
