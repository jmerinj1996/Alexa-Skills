import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import pickle
from collections import Counter
import io

lemmatizer = WordNetLemmatizer()
hm_lines = 100000000

def create_lexicon(pos, neg):
    lexicon_with_duplicates = []
    for file in [pos, neg]:
        with io.open(file, 'r', encoding="cp437") as f:
            contents = f.readlines()
            for l in contents[:hm_lines]:
                all_words = word_tokenize(l.lower())
                lexicon_with_duplicates +=list(all_words)
    lexicon_with_duplicates = [lemmatizer.lemmatize(i) for i in lexicon_with_duplicates]
    w_counts = Counter(lexicon_with_duplicates)

    lexicon = []
    for w in w_counts:
        if 1000 > w_counts[w] > 50:
            lexicon.append(w)
    #print(len(lexicon))
    return lexicon

def sample_sentence(sample, lexicon, classification):
    featureset = []
    with io.open(sample, 'r', encoding = 'cp437') as f:
        contents = f.readlines()
        for l in contents[:hm_lines]:
            sample_words = word_tokenize(l.lower())
            sample_words = [lemmatizer.lemmatize(i) for i in sample_words]
            features = np.zeros(len(lexicon))

            for word in sample_words:
                if word.lower() in lexicon:
                    index_v = lexicon.index(word.lower())
                    features[index_v] +=1
            features = list(features)
            featureset.append([features, classification])
    return featureset

def create_featurset_and_labels(pos, neg, test_size = 0.1):
    lexicon = create_lexicon(pos, neg)
    features = []
    features += sample_sentence(pos, lexicon, [1,0])
    features += sample_sentence(neg, lexicon, [0,1])
    random.shuffle(features)

    features = np.array(features)

    testing_size = int(test_size*len(features))

    train_x = list(features[:,0][:-testing_size])
    train_y = list(features[:,1][:-testing_size])

    test_x = list(features[:,0][testing_size:])
    test_y = list(features[:,1][testing_size:])

    return train_x, train_y, test_x, test_y

if __name__ =='__main__':
    train_x, train_y, test_x, test_y = create_featurset_and_labels('pos.txt', 'neg.txt')
    with open('pos_neg_set.pickle','wb') as f:
        pickle.dump([train_x, train_y, test_x, test_y], f)
