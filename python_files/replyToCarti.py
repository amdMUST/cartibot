#reply to playboi carti when he tweets
import os
import time
import random2
import tweepy as tp
from cartiMain import api

class MyStreamListener(tp.StreamListener):
    def on_status(self, status ):
        print( status.text )
        statusID = status.id
        statusAt = status.user
        if '@playboicarti' in status.text: #@playboicarti
            print('this a double, not tweeting at him!')
            turnOnReplyToCarti(False)
            return
        else:
            api.update_status('@' + statusAt.screen_name + ' ' + getReplyforCarti(), in_reply_to_status_id = statusID ) 
            print('replied to tweet!')
        return
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth = api.auth, listener = myStreamListener)


def replyToCarti():
    print('waiting for the god himself, carti, to tweet!')
    myStream.filter(follow=["101263750"]) # 4318546215 is test filter "101263750" is carti

def turnOnReplyToCarti(bool):
    while bool:
        replyToCarti()
        print('replied! now gonna take 30 sec break!')
        time.sleep(30)

def sizeOfFile(filepath):
    # a method to find number of lines
	#filepath ="TEXT_files\\TXT_replytoCarti.txt" #PC
    filepath = "TEXT_files/TXT_replytoCarti.txt" #MAC
    count = 1
    with open(filepath, encoding="utf8") as f:
        line = f.readline()		
        for line in f:
            count += 1
    return count

def getReplyforCarti():
    #filepath ="TEXT_files\\TXT_replytoCarti.txt" #PC
    filepath = "TEXT_files/TXT_replytoCarti.txt" #MAC
    count = random2.randint(0,sizeOfFile(filepath))
    with open(filepath, encoding="utf8") as f:
        line = f.readline(count)
        lineNum = 0		
        for line in f:
            lineNum += 1
            if count == lineNum:
                linpe = str(line) 
                print(linpe)
                return linpe

while True:
    turnOnReplyToCarti(True)