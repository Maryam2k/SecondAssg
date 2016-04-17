import os

ftrain = open("image_training_full.txt", 'r')
# 784 bif for each pic in each row + 1 integer that represents the value of the image
ftest = open("image_test_full.txt", 'r')
# 784 bif without label
fcombined = open("image_full_combined_small.txt", 'w')
# each test data connects to each train data.
train_records = ftrain.readlines()[0:int(sys.argv[1])]
test_records = ftest.readlines()[0:int(sys.argv[2])]

i=0
for item1 in test_records:
	for item2 in train_records:
		# rstrip returns a copy of the string with trailing characters removed.
		str1 = str(item1).rstrip().split(' ')
		str2 = str(item2).rstrip().split(' ')

		fcombined.write(' '.join(str1[0:785])+" "+' '.join(str2)+"\n")
		i+=1
	if i%100==0:
		os.fsync(fcombined.fileno())


fcombined.close()
