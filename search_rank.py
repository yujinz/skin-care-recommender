import math
import sys
import time
import heapq 
import metapy
import pytoml
import json



class ReviewRanker(metapy.index.RankingFunction):
    """
    Create a new ranking function in Python that can be used in MeTA.
    """
    def __init__(self, c_param=1.0):
        self.c = c_param
        # You *must* call the base class constructor here!
        super(ReviewRanker, self).__init__() #try BM25 otherwise

    def score_one(self, sd):
        """
        You need to override this function to return a score for a single term.
        For fields available in the score_data sd object,
        @see https://meta-toolkit.org/doxygen/structmeta_1_1index_1_1score__data.html
        """
        lamda = sd.num_docs / sd.corpus_term_count
        tfn = sd.doc_term_count * math.log2(1.0 + self.c * sd.avg_dl / sd.doc_size)
        if lamda < 1 or tfn <= 0:
            return 0.0
        numerator = tfn * math.log2(tfn * lamda) \
                        + math.log2(math.e) * (1.0 / lamda - tfn) \
                        + 0.5 * math.log2(2.0 * math.pi * tfn)
        return sd.query_term_weight * numerator / (tfn + 1.0)
        #return (self.param + sd.doc_term_count) / (self.param * sd.doc_unique_terms + sd.doc_size)


def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate.

    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index. You can ignore this, unless
    you need to load a ForwardIndex for some reason...
    """
    #return ReviewRanker(5)
    return metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
    #return metapy.index.DirichletPrior(mu = 515)

def loadData():
    reviewData = {}
    '''return a dictionary
       use line num as key, tuple(asin,rate) as value'''
    auxiliary = open('auxiliary.txt', 'r')
    index = 0
    for line in auxiliary:
        line = line.strip().split('\t')
        reviewData[index] = (line[0],line[1])
        index += 1
    auxiliary.close()
    return reviewData

def combineReviewscore(alpha,results,reviewScore):

    heap = []
    '''use -score as sorting key in heap so it's a max heap'''
    for x in results:
        temp_index = x[0]
        temp_score = x[1]
        score = (1-alpha) * temp_score + alpha * float(reviewScore.get(temp_index)[1])
        heapq.heappush(heap, (-score, reviewScore.get(temp_index)))
    return heap

def getTopK(k,heap):
     valid = min(k,len(heap))
     for i in range(valid):
        temp = heapq.heappop(heap)
        print temp[1][0]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)
    cfg = sys.argv[1]
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    doc_num = idx.num_docs()
    query = metapy.index.Document()
    ranker = metapy.index.OkapiBM25(k1=1.2,b=0.75,k3=500)
    '''set query here, change to user input interface here'''
    query.content("dark spots")

    initial_results = ranker.score(idx, query, doc_num)
    reviewData = loadData()

    '''modify alpha(the influence of the overall score) here'''
    top_results = combineReviewscore(0.3,initial_results,reviewData)

    '''modify how many top results you want'''
    getTopK(3,top_results)

    
 
    
