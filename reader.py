import json

f = open('reviews_Beauty_5.json', 'r')
asin = open('asin.txt', 'w')
reviewText = open('reviewText.txt', 'w')
overall = open('overall.txt', 'w')
for line in f:
    data = json.loads(line)
    asin.write(str(data['asin']) + '\n')
    reviewText.write(str(data['reviewText']) + '\n')
    overall.write(str(data['overall']) + '\n')
