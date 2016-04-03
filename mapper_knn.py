#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    # words = line.split()
    input_key = line[0:3]
    # increase counters
    # for word in line:        
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (input_key, line[4:])

