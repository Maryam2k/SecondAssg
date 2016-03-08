#!/usr/bin/env python

import sys
import re
for line in sys.stdin:
    line = line.strip()
    new_string = re.sub('[^A-Za-z0-9]+',' ', line)


    words = new_string.split()
    for word in words:    
        print '%s\t%s' % (len(word), word)
