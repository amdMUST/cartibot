
import tweepy as tp # to use the twitter API
import time # to specify how much time in between tweets
import os # to move to the cartiPics folder

# creds to login to api
consumerKey = 'NdFFEbjRY3P1V0mgNz3rAzTHN'
consumerSec = 'hHwErqiswcARJeCjSQWG6DP5j1zlPkoblh3UbQTxGTAcq9PA8o'
accessTok = '1174077014275502080-Kpg7KmUFSSyQVfuqm8jbABli5g7aEf'
accessSec = 'nNDhR5kjtZdLLSx8UX70J45YXVkoVa7LB3IhrUe5uFHHl'

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