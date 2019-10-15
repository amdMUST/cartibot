import os
import time
import random2
import tweepy as tp
from replyToCarti import turnOnReplyToCarti
from cartiGetLyric import turnOnTweetLyric
from cartiReply import turnOnReplyToTweets
from replytoCartiKeyword import turnOnReplyKeywordCarti


# time conversions
    # 1 minute 60
	# 30 minutes 1800
	# 1 hour 3600

# this is the main true statement
while True:
    turnOnReplyToTweets(60) # this is going to respond to whenever someone tweets at cartibot, on a 15 sec timer rn
    turnOnTweetLyric(60) # this is parsing carti lyrics from a file and tweeting them out every 30min or 1 hour
    turnOnReplyToCarti() #reply to playboi carti when he tweets
    turnOnReplyKeywordCarti(True) # reply to people who have the word carti in their tweet