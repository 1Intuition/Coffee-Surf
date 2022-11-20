import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import SnowballStemmer
import pickle
from operator import itemgetter
import time
#lemmatizer = WordNetLemmatizer()

stemmer = SnowballStemmer(language = "english")

DF = pickle.load(open("df.p", "rb"))
WORDS = pickle.load(open("words.p", "rb"))

def get_words(description):
    l = []
    try:
        words = nltk.word_tokenize(description.lower().replace("-"," "))
        #print(words)
        tagged = nltk.pos_tag(words)
        for i in tagged:
            if i[0] not in [",",".","!","?",":",";"]:
                l.append(stemmer.stem(i[0]))
        #print(tagged)


    except Exception as e:
        print(str(e))

    return l

def one_hot(description):
    features = get_words(description)
    vector = [1 if i in features else 0 for i in WORDS]
    return vector

def search(query):
    vector = one_hot(query)
    pairs = []
    for i,j in zip(DF["coffee"],DF["all_words"]):
        pairs.append([i,j,np.dot(vector,j)])
    pairs.sort(key=itemgetter(2))
    return [i[0] for i in pairs[0:10]]

start = time.time()
print(search("chocolaty, vanilla paste, Ethiopia"))
end = time.time()
print(end - start)


