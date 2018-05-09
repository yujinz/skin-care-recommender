import json
import codecs

f = open('product_based_data.json', 'r')

auxiliary = open('auxiliary.txt', 'w')
asin = open('asin.txt', 'w')
reviewText = open('reviewText.txt', 'w')

idx = 0
for line in f:
    data = json.loads(line)
    reviewText.write(u''.join(data['reviewText']).encode('utf-8') + '\n')
    auxiliary.write(data['asin'] +'\t' +str(data['overall']) + '\n')
    asin.write(str(data['asin']) + '\n')

auxiliary.close()
asin.close()
