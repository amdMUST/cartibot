# reply to people who have the word carti in their tweet
import os
import time
import random2
import tweepy as tp
from cartiMain import api


class MyStreamListener(tp.StreamListener):
    def on_status(self, status, include_my_retweet=False ):
        print( status.text )
        statusID = status.id
        statusAt = status.user
        #retweet = include_my_retweet
        #if retweet = False: #@playboicarti
        #    print('this a rt, does not count!')
            #turnOnReplyKeywordCarti(False)
        #    return
        #else:
        api.update_status('@' + statusAt.screen_name + ' ' + getReply(), in_reply_to_status_id = statusID ) 
        print('replied to tweet!')
        return
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tp.Stream(auth = api.auth, listener = myStreamListener)


def sizeOfFile():
    # a method to find number of lines
	filepath ="TEXT_files\\TXT_replytoPPL.txt"
	count = 1
	with open(filepath, encoding="utf8") as f:
		line = f.readline()		
		for line in f:
			count += 1
	return count

def getReply():
    count = random2.randint(0,sizeOfFile())
    filepath ="TEXT_files\\TXT_replytoPPL.txt"
    with open(filepath, encoding="utf8") as f:
        line = f.readline(count)
        lineNum = 0		
        for line in f:
            lineNum += 1
            if count == lineNum:
                linpe = str(line) 
                print(linpe)
                return linpe

def whoTweetingCarti():
    print('looking for people who have said carti!')
    myStream.filter(track=['carti'], is_async=True,filter_level='medium',languages='en')

#def turnOnReplyKeywordCarti(bool):
#    while bool:
#        whoTweetingCarti()

while True:
    whoTweetingCarti()
#    turnOnReplyKeywordCarti(True)