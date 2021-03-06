#!/usr/bin/env python

from operator import itemgetter
import sys,re
import math
import operator



# key is test data ,Value is predicted label
# input comes from STDIN

#test_record = [1*784]
#train_list = [(1*784,label),...]
#This function updates the train_list to [(1*784,label, distance),..] where
#distance is the distance to the test data
def classify(test_record, train_list):

    #distances = []
    class_freq = [0]*10


    train_list = [(float(x[0]),x[1]) for x in train_list]
    #print train_list
    #sort the training records based on distance 0:783(attributes),784(class), 785(distance) 

   
    train_list = sorted(train_list, key=operator.itemgetter(0))  

    #the closest 
    train_list = train_list[0:k]
    # k is the number of nearest neghbor

    #print train_list    

    # find the majority class
    for i in range(0,len(train_list)):
        # label of the ith training record from k closset one=
        # int(train_list[i][attribute_count])
        class_freq[int(train_list[i][1])] +=1/(float(train_list[i][0])+0.1)

    #print class_freq
    max_value = max(class_freq)
    max_index = class_freq.index(max_value)


    return max_index


train_list = []
prior_test_record = None
test_record = None
train_record = None
k=12
attribute_count = 784 

for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    #print line
    # parse the input we got from mapper.py
    test_record, train_record = line.split("\t", 1)
    train_record_splitted = train_record.rstrip().split(' ')

    if prior_test_record == None: #first-line
        prior_test_record = test_record

    if prior_test_record == test_record:
        train_list.append(train_record_splitted)

    else:
        test_record_splitted= prior_test_record.rstrip().split(' ')  
        predicted_label = classify(test_record_splitted[0:attribute_count], train_list)
        actual_label = test_record_splitted[attribute_count]
        print '%s\t%s' % (actual_label,predicted_label) 

        train_list = []
        #print '%s\t%s' % (prior_test_record,predicted_label)
        prior_test_record = test_record

#print 'hey', test_record

test_record_splitted= test_record.rstrip().split(' ')      
predicted_label = classify(test_record_splitted[0:attribute_count], train_list)
actual_label = test_record_splitted[attribute_count]
print '%s\t%s' % (actual_label,predicted_label)

