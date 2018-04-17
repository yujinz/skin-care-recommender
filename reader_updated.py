import json

f = open('reviews_Beauty_5.json', 'r')
asin = open('asin.txt', 'w')
reviewText = open('reviewText.txt', 'w')
overall = open('overall.txt', 'w')
result = open('result.txt', 'w')
for line in f:
    data = json.loads(line)
    asin.write(str(data['asin']) + '\n')
    reviewText.write(str(data['reviewText']) + '\n')
    overall.write(str(data['overall']) + '\n')
    result.write(str(data['reviewText']) + '\t' + str(data['asin']) + '\t' + str(data['overall']) + '\n')
