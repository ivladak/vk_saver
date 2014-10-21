#!/usr/bin/python

# This version allows to keep original song names
# but the setup is a little bit more involoved.

# Usage: open a vk page containing the music files
# open javascript console in your browser
# run the vkSaver.js script
# save it's outputs as your_source.html 
# edit it if needed
# ./vk_saver yourSouce.html
# enjoy

from re import *
import re
import sys
from subprocess import * 
regex = re.compile("3pm\.[^\"]+?/:sptth")

if len(sys.argv) < 2:
	print "please specify source html file"
	exit()	

for line in open(sys.argv[1]):
	link = line[0:line.find(" ")]
	filename = line[line.find(" ") + 1:-1].strip() + ".mp3"
	filename = 	re.sub(r'/', ',', filename)
	filename = 	re.sub(r"'", '', filename)
	filename = 	re.sub(r"\|", '', filename)
#	call["wget", "--no-clobber", "-O", filename, link]
#	line = line[::-1]
#	song_tuple = map (lambda s: s[::-1], regex.findall(line))
#	for song in song_tuple: 
	p = Popen(["wget", "--no-clobber", "-O", filename, link], stdout=PIPE)
	print(p.communicate()[0])
