f = open('output_updated.json', 'r')

fw = open('crawled_reviews_Beauty_5.json', 'w')
startidx = 0
endidx = 1
for line in f:
    print(len(line))
    while endidx < len(line):
        startidx = line.find('{"')
        endidx = line.find('},')
        if endidx == -1:
            fw.write(line[startidx:])
            break
        fw.write(line[startidx:endidx + 1] + '\n')
        line = line[endidx+1:]