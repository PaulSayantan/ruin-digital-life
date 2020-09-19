import os
import tweepy
from dotenv import load_dotenv

load_dotenv(verbose=True)

auth = tweepy.OAuthHandler(os.getenv("API_KEY"),
    os.getenv("API_SECRET_KEY"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), 
    os.getenv("ACCESS_SECRET_TOKEN"))


#api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

user = api.get_user("FenilJain7")

print("User details:")
print(user.id)
print(user.name)
print(user.description)
print(user.location)

direct_mssg = api.send_direct_message(user.id, "Hello, Fenil, I am your lovely scary twitter bot!")
print(direct_mssg.message_create['message_data']['text'])

try:
    api.verify_credentials()
    #api.update_status("Test tweet from my twitter bot")
    print("Authentication OK")
except:
    print("Error during authentication")
