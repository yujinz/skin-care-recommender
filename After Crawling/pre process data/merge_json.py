import glob 
import json 

files = glob.glob('*.json')
output = open('output.json', 'w')
result = [] 
for file in files:
	f = open(file,'r')
	for line in f:
		output.write(line)

print(output)