#reply to playboi carti when he tweets
import os
import time
import random2
import tweepy as tp
from cartiMain import api, myStream


def replyToCarti():
    print('waiting for the god himself, carti, to tweet!')
    myStream.filter(follow=["4318546215"]) # 4318546215 is test filter "101263750" is carti

def turnOnReplyToCarti():
    replyToCarti()


while True:
    turnOnReplyToCarti()