# will reply to people who tweet to carti bot
import tweepy as tp 
import os
import time
import random2
from cartiMain import api, auth
 
#https://twitter.com/search?q=carti&src=typed_query&f=live

mentions = api.mentions_timeline()
mentions[0].__dict__.keys()
mentions[0].text


# this stores the last seen id
#fileName = 'TEXT_files\\TXT_cartiLastSeenID.txt' #PC
fileName = 'TEXT_files/TXT_cartiLastSeenID.txt' #MAC

def sizeOfFile():
    # a method to find number of lines
    #filepath ="TEXT_files\\TXT_replytoPPL.txt" #PC
    filepath = "TEXT_files/TXT_replyToPPL.txt" #MAC
    count = 1
    with open(filepath, encoding="utf8") as f:
        line = f.readline()		
        for line in f:
            count += 1
    return count

def getReply(count):
    #filepath ="TEXT_files\\TXT_replytoPPL.txt" #PC
    filepath = "TEXT_files/TXT_replyToPPL.txt" #MAC
    with open(filepath, encoding="utf8") as f:
        line = f.readline(count)
        lineNum = 0		
        for line in f:
            lineNum += 1
            if count == lineNum:
                linpe = str(line) 
                print("response: " + linpe)
                return linpe

def replyToTweet(statusId,username):
    fileSize = sizeOfFile()
    x = random2.randint(0,fileSize)
    api.update_status('@' + username + ' ' + getReply(x), in_reply_to_status_id = statusId)
    print('tweeted!')

def likeTweet(statusId,username):
    api.create_favorite(statusId)
    print('liked the tweet!')

class MyStreamListener(tp.StreamListener):
    
    def on_status(self,status):
        username = status.user.screen_name
        statusId = status.id
        print( " @"  + username + ": " +  status.text )
        replyToTweet(statusId,username)
        likeTweet(statusId,username)


my_stream_listener = MyStreamListener()
stream = tp.Stream(auth, my_stream_listener)
print('waiting for mfs to @ me')
stream.filter(track=['@cartibotslatt'])
time.sleep(300)




#while True:
#    turnOnReplyToTweets(300)