# will reply to people who tweet to carti bot
import tweepy as tp 
import os
import time
from cartiMain import api
import random2
 
#https://twitter.com/search?q=carti&src=typed_query&f=live

mentions = api.mentions_timeline()
mentions[0].__dict__.keys()
mentions[0].text

flush = True

for mention in mentions:
    print( str(mention.id) + ' - ' + mention.text)
    if 'slat' in mention.text.lower():
        print('gonna respond 1')
    elif 'slime' in mention.text.lower():
        print('gonna respond 2')

# this stores the last seen id
fileName = 'TEXT_files\TXT_cartiLastSeenID.txt'

#phrases
slime =' jus chillin my slime praise to carti*!^'
slat = ' slat on my momma we WANT WHOLE LOTTA RED!!^!*'

def sizeOfFile():
    # a method to find number of lines
	filepath ="TEXT_files\TXT_replytoPPL.txt"
	count = 1
	with open(filepath, encoding="utf8") as f:
		line = f.readline()		
		for line in f:
			count += 1
	return count

def getReply(count):
    filepath ="TEXT_files\TXT_replytoPPL.txt"
    with open(filepath, encoding="utf8") as f:
        line = f.readline(count)
        lineNum = 0		
        for line in f:
            lineNum += 1
            if count == lineNum:
                linpe = str(line) 
                print(linpe)
                return linpe

def retrieveLastSeenId(fileName):
    fRead = open(fileName,'r')
    lastSeenId = int(fRead.read().strip())
    fRead.close()
    return lastSeenId

def storeLastSeenId(lastSeenId,fileName):
    fWrite = open(fileName,'w')
    fWrite.write(str(lastSeenId))
    fWrite.close()
    return

def replyToTweets(counter):
# this reverses the order at which it responds to tweets so it responds to early tweets first
    print('tryna retrieve and respond rn bro')
    lastSeenId = retrieveLastSeenId(fileName)
    mentions = api.mentions_timeline(lastSeenId,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        lastSeenId = mention.id
        storeLastSeenId(lastSeenId,fileName)
        if 'slime' in mention.full_text.lower():
            print('spinning the wheel for response')
            api.update_status('@' + mention.user.screen_name + ' ' + getReply(counter), in_reply_to_status_id = lastSeenId)
            counter += 1
        else:
            print('spinning the wheel for response')
            api.update_status('@' + mention.user.screen_name + ' ' + getReply(counter), in_reply_to_status_id = lastSeenId)
            counter += 1

#COME BACK AND TURN ON
while True:
    fileSize = sizeOfFile()
    x = random2.randint(0,fileSize)
    while x < fileSize:
        x += 1
        replyToTweets(x)
        time.sleep(15)
        print('tickR')
        if x >= fileSize:
            x = 0
            continue