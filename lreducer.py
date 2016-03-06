#!/usr/bin/env python

from operator import itemgetter
import sys


current_length = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()

    len_word, word = line.split('\t', 1)
    if current_length == len_word:
        current_count += 1
    else:
        if current_length:
            print '%s\t%s' % (current_length, current_count)
        current_count = 1
        current_length = len_word

if current_length == len_word:
    print '%s\t%s' % (current_length, current_count)


