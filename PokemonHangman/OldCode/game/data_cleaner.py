import re

input_file = open('../data/raw_data.dat','r')
output_file = open('../data/clean_data.dat','w')
while True:
	liner = input_file.readline()
	if liner == None:
		break
	details = liner.split()
	number = int(details[0])
	pokemon = re.sub("[^a-zA-Z']", "",  details[1])
	linew = str(number)+' '+pokemon+'\n'
	output_file.write(linew)
input_file.close()
output_file.close()