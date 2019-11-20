# parsing carti lyrics from a file
# 2 77 109 172 198 248 
import os
import time
import random2
import schedule
import tweepy as tp
from cartiMain import api

# 1 minute 60
# 30 minutes 1800
# 1 hour 3600
#time.sleep(timer)

def turnOnTweetLyric():
	print('turned on, gonna tweet lyric soon!')
	fileSize = sizeOfFile()
	x = random2.randint(0,fileSize)
	if (x < fileSize):
		x = random2.randint(0,fileSize)
		print('tick')
		cartiTweetStatus( getLyric(x,filepath) )
		print('tweeted lyric!')
		
	elif (x >= fileSize):
		x = 0
		print('went past the total amount of lines, gonna reset to 0 !')

def sizeOfFile():
# a method to find number of lines
	#filepath = 'TEXT_files\\TXT_cartiLyrics.txt' #PC
	filepath = 'TEXT_files/TXT_cartiLyrics.txt' #MAC
	count = 1
	with open(filepath, encoding="utf8") as f:
		line = f.readline()		
		for line in f:
			count += 1
	return count

#filepath = 'TEXT_files\\TXT_cartiLyrics.txt' #PC
filepath = 'TEXT_files/TXT_cartiLyrics.txt' #MAC
def getLyric(count,filepath):
	with open(filepath, encoding="utf8") as f:
		line = f.readline(count).strip()
		lineNum = 0		
		for line in f:
			lineNum += 1
			if count == lineNum:
				print(line)
				return line

def cartiTweetStatus(x):
	api.update_status( x.lower() )

# uk time its in, i want everyday at 10am-3pm, 1pm-6pm, 5pm-10pm 9pm-2am +++ 
schedule.every().day.at("15:00").do(turnOnTweetLyric) # 10am --> 3pm
schedule.every().day.at("18:00").do(turnOnTweetLyric) # 1pm --> 6pm
schedule.every().day.at("22:00").do(turnOnTweetLyric) # 5pm --> 10pm
schedule.every().day.at("02:00").do(turnOnTweetLyric) # 9pm --> 2am

while True:
	#turnOnTweetLyric()
	#scheduleTweets()
	schedule.run_pending()
	time.sleep(1)