import json

# fop = open('output2.json', 'r')
# for line in fop:
#     print(line)

def read_json(*args):

    result = {}

    for input in args:
        fop = open(input)
        for line in fop:
            # print(line)
            data = json.loads(line)
            key = data['asin']
            if key not in result:
                result[key] = {}
                result[key]['asin'] = data['asin']
                result[key]['reviewText'] = [data['reviewText']]
                result[key]['overall'] = [int(data['overall'])]
            else:
                result[key]['reviewText'].append(data['reviewText'])
                result[key]['overall'].append(int(data['overall']))
        fop.close()

    for key in result:
        # print(result[key]['overall'])
        result[key]['overall'] = sum(result[key]['overall'])/len(result[key]['overall'])

    return result


# read_json(file1, file2, file3....)
result = read_json('crawled_reviews_Beauty_5.json')
f_write = open('product_based_data.json', 'w')
for key in result:
    f_write.write(json.dumps(result[key]) + '\n')
f_write.close()

# print(average(result['B000P20RAQ']['overall']))