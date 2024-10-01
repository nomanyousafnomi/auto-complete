from pprint import pprint
import simplejson as json
import sys 
from nltk.corpus import brown
from nltk.corpus import reuters
import nltk
from nltk.corpus import PlaintextCorpusReader

class Suggestion():

    def get_trigram_freq(self, tokens):
        tgs = list(nltk.trigrams(tokens))

        a, b, c = list(zip(*tgs))
        bgs = list(zip(a, b))
        return nltk.ConditionalFreqDist(list(zip(bgs, c)))

    def get_bigram_freq(self, tokens):
        bgs = list(nltk.bigrams(tokens))
        return nltk.ConditionalFreqDist(bgs)

    def appendwithcheck(self, preds, to_append):
        for pred in preds:
            if pred[0] == to_append[0]:
                return
        preds.append(to_append)

    def incomplete_pred(self, words, n):
        all_succeeding = bgs_freq[(words[n-2])].most_common()
        preds = []
        number = 0
        for pred in all_succeeding:
            if pred[0].startswith(words[n-1]):
                self.appendwithcheck(preds, pred)
                number += 1
            if number == 3:
                return preds
        if len(preds) < 3:
            med = []
            for pred in all_succeeding:
                med.append((pred[0], nltk.edit_distance(
                    pred[0], words[n-1], transpositions=True)))
            med.sort(key=lambda x: x[1])
            index = 0
            while len(preds) < 3:
                print(index, len(med))
                if index < len(med):
                    if med[index][1] > 0:
                        self.appendwithcheck(preds, med[index])
                    index += 1
                if index >= len(preds):
                    return preds
        return preds
