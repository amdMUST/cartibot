# will reply to people who tweet carti
import tweepy as tp 
import os
from cartiMain import api
import time
 
#https://twitter.com/search?q=carti&src=typed_query&f=live


mentions = api.mentions_timeline()
mentions[0].__dict__.keys()
mentions[0].text

flush = True

for mention in mentions:
    print( str(mention.id) + ' - ' + mention.text)
    #if ( ('slime' in mention.text.lower()) and ('slat' in mention.text.lower()) ):
        #print('ight i see u slime, keep it slat!***')
    if 'slat' in mention.text.lower():
        print('slat on my momma we WANT WHOLE LOTTA RED!!^!*')
    elif 'slime' in mention.text.lower():
        print('jus chillin my slime praise to carti*!^')

# this stores the last seen id
fileName = 'cartiReplytextfile.txt'

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

def replyToTweets():
# this reverses the order at which it responds to tweets so it responds to early tweets first
    print('tryna retrieve and respond rn bro')
    lastSeenId = retrieveLastSeenId(fileName)
    mentions = api.mentions_timeline(lastSeenId,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        lastSeenId = mention.id
        storeLastSeenId(lastSeenId,fileName)
        if 'slime' in mention.full_text.lower():
            print('tryna respond rn bro')
            api.update_status('@' + mention.user.screen_name + 'jus chillin my slime praise to carti*!^')
        elif 'slat' in mention.full_text.lower():
            print('tryna respond rn bro')
            api.update_status('@' + mention.user.screen_name + 'slat on my momma we WANT WHOLE LOTTA RED!!^!*')
        #elif  ( ('slime' in mention.full_text.lower()) and ('slat' in mention.full_text.lower()) ):
         #   print('tryna respond rn bro')
         #   api.update_status('@' + mention.user.screen_name + 'ight i see u slime, keep it slat!***')

while True:
    replyToTweets()
    time.sleep(15)