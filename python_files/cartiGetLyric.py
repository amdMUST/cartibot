# parsing carti lyrics from a file
# 2 77 109 172 
import os
import time
import random2

def sizeOfFile():
# a method to find number of lines
	filepath ="TEXT_files\TXT_cartiLyrics.txt"
	count = 1
	with open(filepath, encoding="utf8") as f:
		line = f.readline()		
		for line in f:
			count += 1
	return count

filepath ="TEXT_files\TXT_cartiLyrics.txt"
def getLyric(count,filepath):
	with open(filepath, encoding="utf8") as f:
		line = f.readline(count).strip()
		lineNum = 0		
		for line in f:
			lineNum += 1
			if count == lineNum:
				print(line)
				return line

fileSize = sizeOfFile()
x = 0
while x < fileSize:
	x += 1
	print('tickCGL')
	getLyric(x,filepath)

	# 1 minute 60
	time.sleep(6)

	# 30 minutes 1800
	#time.sleep(1800)

	# 1 hour 3600
	#time.sleep(3600)
	
	if x >= fileSize:
		x = 0
		# print('bro pls loop here like bro please loop here like please bro im begging u')
		continue