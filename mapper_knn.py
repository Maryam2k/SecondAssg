#!/usr/bin/env python

import sys
import re
import os, math

attribute_count = 784 
#in mapper key is a test data. Value is traing data+it's label
for line in sys.stdin:
    #print os.environ["map.input.file"]
    #print line
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split()
    
    #test[0:783] [784][785]
    test_record = line[0:attribute_count]
    test_label = line[attribute_count]

    train_record = line[attribute_count+1:2*attribute_count+1]
    train_label = line[2*attribute_count+1]

    
    #print test_label,' ', train_label

    distance = 0
    for i in range(0,attribute_count):
            distance += math.pow(int(test_record[i]) - int(train_record[i]), 2)
    distance=math.sqrt(distance)
    distance = str(round(distance,2))

    
    test_record = ' '.join(test_record)

    print '%s\t%s' % (test_record+" "+test_label, distance+" "+train_label)



#small file
# cat  /Users/mrym/Dropbox/mehrdad/image_combined.txt | python /Users/mrym/Desktop/bigData/SecondAssg/mapper_knn.py |sort -k1,1 | python /Users/mrym/Desktop/bigData/SecondAssg/reducer_knn.py

#large file
#cat  /Users/mrym/Desktop/image_full_combined_small.txt | python /Users/mrym/Desktop/bigData/SecondAssg/mapper_knn.py |sort -k1,1 | python /Users/mrym/Desktop/bigData/SecondAssg/reducer_knn.py


