# parsing carti lyrics from a file
# 2 77 109 172 198 248 
import os
import time
import random2
import tweepy as tp
from cartiMain import api


def turnOnTweetLyric(timer):
	print('turned on, gonna tweet lyric soon!')
	fileSize = sizeOfFile()
	x = random2.randint(0,fileSize)
	while x < fileSize:
		x = random2.randint(0,fileSize)
		print('tick')
		cartiTweetStatus( getLyric(x,filepath) )
		print('tweeted lyric!')

		# 1 minute 60
		# 30 minutes 1800
		# 1 hour 3600
		time.sleep(timer)
		
		if x >= fileSize:
			x = 0
			print('went past the total amount of lines, gonna reset to 0 !')
			continue

def sizeOfFile():
# a method to find number of lines
	filepath ="TEXT_files\\TXT_cartiLyrics.txt"
	count = 1
	with open(filepath, encoding="utf8") as f:
		line = f.readline()		
		for line in f:
			count += 1
	return count

filepath ="TEXT_files\\TXT_cartiLyrics.txt"
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
