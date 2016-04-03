#!/usr/bin/env python
from operator import itemgetter
import sys,re
import math
import operator
current_key = None
value_splitted = [0,0,0]
train_list=[]
class_freq=[0]*10
k=3

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split("\t", 1)
    value_splitted = value.split(",")


    if current_key == None: #first-line
        current_key = key


    if current_key == key:
        train_list.append(value_splitted)

    else:
        distances = []
        key_splitted = current_key.split(",")

        #compute distances for each training record
        for item in train_list:
            distance = math.sqrt((int(key_splitted[0]) - int(item[0]))**2+ (int(key_splitted[1]) - int(item[1]))**2)
            distances.append(round(distance,2))

        # join the training_list and distances    
        for item in range(0,len(train_list)):
            train_list[item].append(distances[item])

        train_list = sorted(train_list, key=operator.itemgetter(3),reverse =False)  
        train_list = train_list[0:k]
        

        for i in range(0,len(train_list)):
            class_freq[int(train_list[i][2])] = class_freq[int(train_list[i][2])]+1

        
        max_num = 0
        max_index = 0
        for i in range(0,len(class_freq)):
            if class_freq[i]>max_num:
                max_num = class_freq[i]
                max_index = i
            
        print '%s\t%s' % (current_key, max_index)



        class_freq= [0]*10    
        train_list = []
        current_key=key
        distances = []
        train_list.append(value_splitted)
    # print train_list


distances = []
key_splitted = current_key.split(",")

for item in train_list:
    distance = math.sqrt((int(key_splitted[0]) - int(item[0]))**2+ (int(key_splitted[1]) - int(item[1]))**2)
    distances.append(round(distance,2))

for item in range(0,len(train_list)):
    train_list[item].append(distances[item])

train_list = sorted(train_list, key=operator.itemgetter(3),reverse =False)  
train_list = train_list[0:k]

for i in range(0,len(train_list)):
            class_freq[int(train_list[i][2])] = class_freq[int(train_list[i][2])]+1

max_num = 0
max_index = 0
for i in range(0,len(class_freq)):
    if class_freq[i]>max_num:
        max_num = class_freq[i]
        max_index = i

print '%s\t%s' % (current_key, max_index)



