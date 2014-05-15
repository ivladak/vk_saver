#!/usr/bin/python

# usage: save an html file containing mp3 links from vk.com 
# ("view source" in your web browser (ctrl+u in Chrome))
# ./vk_saver your.html
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
	line = line[::-1]
	song_tuple = map (lambda s: s[::-1], regex.findall(line))
	for song in song_tuple: 
		p = Popen(["wget", "--no-clobber", song], stdout=PIPE)
		print(p.communicate()[0])
