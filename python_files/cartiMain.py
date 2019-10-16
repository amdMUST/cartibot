# was original main method, but now is pretty much just for API login and MyStreamListener class
import tweepy as tp # to use the twitter API
import time # to specify how much time in between tweets
import os # to move to the cartiPics folder
from config.py import consumerKey,consumerSec,accessTok,accessSec


# loging in
auth = tp.OAuthHandler(consumerKey,consumerSec)
auth.set_access_token(accessTok,accessSec)
api = tp.API(auth)

#overriding tweepy.StreamListener to add logic to on_status
class MyStreamListener(tp.StreamListener):
    def on_status(self, status ):
        print( status.text )
        print('replied to tweet!')
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth = api.auth, listener = myStreamListener)