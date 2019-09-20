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

#phrases
slime =' jus chillin my slime praise to carti*!^'
slat = ' slat on my momma we WANT WHOLE LOTTA RED!!^!*'
og = ' i\'m an OG. i was an OG when i was 16. i was an OG when i made the decision I don\'t want to go to school anymore and start skipping to make music.'
slatslime = ' ight i see u slime, keep it slat!***'
navimg = 'nav1.jpeg'

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
            print('slime response')
            api.update_status('@' + mention.user.screen_name + slime, in_reply_to_status_id = lastSeenId)       
        elif 'slat' in mention.full_text.lower():
            print('slat response')
            api.update_status('@' + mention.user.screen_name + slat, in_reply_to_status_id = lastSeenId)
        elif  ( ('slime' and 'slat' in mention.full_text.lower() ) ):
            print('slime slat')
            api.update_status('@' + mention.user.screen_name + slatslime, in_reply_to_status_id = lastSeenId)
        elif 'nav' in mention.full_text.lower():
            print('nav response')
            api.update_with_media(navimg,'@' + mention.user.screen_name + slime, in_reply_to_status_id = lastSeenId)    
        else:
            print('og respose')
            api.update_status('@' + mention.user.screen_name + og, in_reply_to_status_id = lastSeenId)


while True:
    replyToTweets()
    time.sleep(15)
    print('1tick')