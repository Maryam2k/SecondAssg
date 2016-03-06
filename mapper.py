#!/usr/bin/env python

import sys
# import re

my_list = ["_","~","!","@","#","$","%","^","&","*","(",")","-","=","+","/",">",".","?","|","<",",","`",":","}","[","]",
";","{","\\"]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # newWord = re.sub(r'[^\w\s]', '', word)
        for i in my_list:
             word = word.replace(i,'')
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word , 1)