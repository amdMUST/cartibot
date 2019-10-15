
import tweepy as tp # to use the twitter API
import time # to specify how much time in between tweets
import os # to move to the cartiPics folder
from config import consumerKey,consumerSec,accessTok,accessSec

# loging in
auth = tp.OAuthHandler(consumerKey,consumerSec)
auth.set_access_token(accessTok,accessSec)
api = tp.API(auth)

# this will be the head place where we start call all the methods to run

#while True:
#    replyToTweets()
#    #time.sleep(0)

#x = 0
#fileSize = sizeOfFile()
#while x < fileSize:
	#x += 1
	#print('tick')
	#getLyric(x)

	# 1 minute 60
	#time.sleep(60)

	# 30 minutes 1800
	#time.sleep(1800)

	# 1 hour 3600
	#time.sleep(3600)
	
	#if x >= fileSize:
	#	x = 0
		# print('bro pls loop here like bro please loop here like please bro im begging u')
	#	continue