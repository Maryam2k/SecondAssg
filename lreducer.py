#!/usr/bin/env python

# from operator import itemgetter
# import sys


# current_length = None
# current_count = 0
# word = None
# allWords = []

# for line in sys.stdin:
#     line = line.strip()

#     len_word, word = line.split('\t', 1)
#     if current_length == len_word:
#         current_count += 1
#         allWords.append(word)


#     else:
#         if current_length:
#             # write result to STDOUT
#             print '%s\t%s' % (current_length, allWords)
#         current_count = 1
#         current_length = len_word

# if current_length == len_word:
#     print '%s\t%s' % (current_length, allWords)


#!/usr/bin/env python

from operator import itemgetter
import sys,re

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split("\t", 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
