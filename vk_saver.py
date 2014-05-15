#!/usr/bin/python

# usage: save an html file containing mp3 links from vk.com 
# ("view source" in your web browser (ctrl+u in Chrome))
# ./vk_saver < your.html
# enjoy

from re import *
import re
import sys
from subprocess import call
regex = re.compile("3pm\.[^\"]+?/:sptth")

for line in sys.stdin:
	line = ''.join(reversed(line))
	song_tuple = map (lambda s: "".join(reversed(s)), regex.findall(line))
	for song in song_tuple: 
		call(["wget -c", song])
