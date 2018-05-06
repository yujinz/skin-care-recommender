import json

f = open('reviews_Beauty_5.json', 'r')

auxiliary = open('auxiliary.txt', 'w')
asin = open('asin.txt', 'w')

for line in f:
    data = json.loads(line)
    auxiliary.write(data['asin'] +'\t' +str(data['overall']) + '\n')
    asin.write(str(data['asin']) + '\n')
auxiliary.close()
asin.close()
