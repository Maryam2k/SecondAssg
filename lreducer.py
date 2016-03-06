#!/usr/bin/env python

from operator import itemgetter
import sys


current_word = None
current_count = 0
word = None
total = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    len_word, word = line.split('\t', 1)
    total+=1
    print '%s\t%s' % (len_word, total)



    #word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    # try:
    #     words = int(len_word)
    #     # print word
    # except ValueError:
    #      # count was not a number, so silently
    #      # ignore/discard this line
    #      continue

     # this IF-switch only works because Hadoop sorts map output
     # by key (here: word) before it is passed to the reducer
    # if current_word == words:
    #     print current_word
    #     current_count += words
        
    # else:
    #     if current_word:
    #          # write result to STDOUT
    #         print '%s\t%s' % (current_word, current_count)
    #     current_count = words
    #     current_word = len_word

 # do not forget to output the last word if needed!
# if current_word == len_word:
#     print '%s\t%s' % (current_word, current_count)