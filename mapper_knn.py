#!/usr/bin/env python

import sys
import re
import os

attribute_count = 785 
#in mapper key is a test data. Value is traing data+it's label
for line in sys.stdin:
    #print os.environ["map.input.file"]

    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split()
    input_key = ' '.join(line[0:attribute_count])
    input_value = ' '.join(line[attribute_count:])

    print '%s\t%s' % (input_key, input_value)



#small file
# cat  /Users/mrym/Dropbox/mehrdad/image_combined.txt | python /Users/mrym/Desktop/bigData/SecondAssg/mapper_knn.py |sort -k1,1 | python /Users/mrym/Desktop/bigData/SecondAssg/reducer_knn.py

#large file
#cat  /Users/mrym/Desktop/image_full_combined_small.txt | python /Users/mrym/Desktop/bigData/SecondAssg/mapper_knn.py |sort -k1,1 | python /Users/mrym/Desktop/bigData/SecondAssg/reducer_knn.py


