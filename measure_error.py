f = open('/Users/mrym/mehrdad100-1000.txt', 'r')

lines = f.readlines()

counter=0
for line in lines:
	splitted_line = line.split()
	if splitted_line[0]!=splitted_line[1]:
		counter+=1

print 'test_error (%)', (float(counter)/len(lines))*100
