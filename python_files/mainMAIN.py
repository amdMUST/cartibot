import os
import time
import random2
import tweepy as tp
from cartiMain import api

#overriding tweepy.StreamListener to add logic to on_status
class MyStreamListener(tp.StreamListener):

    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
    

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth = api.auth, listener = myStreamListener)

#myStream.filter(track=['carti'], is_async=True)
replyToPWTACarti()

myStream.filter(follow=["101263750"])
replyToCarti()