from __future__ import division
import poetry
import re
from nltk.corpus import cmudict
d = cmudict.dict()
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import *
suffdict = LazyCorpusLoader(
    'cmusuffdict', CMUDictCorpusReader, ['cmusuffdict'])
suffdict = suffdict.dict()


def suffdict_phonemes(word):
    # Use my cmu-based last syllable dictionary
    if re.search("((?i)[bcdfghjklmnpqrstvwxz][aeiouy]+[bcdfghjklmnpqrstvwxz]*e?('[a-z]{1,2})?)(?![a-zA-Z]+)", word.lower()):
        last_syl = re.search("((?i)[bcdfghjklmnpqrstvwxz][aeiouy]+[bcdfghjklmnpqrstvwxz]*e?('[a-z]{1,2})?)(?![a-zA-Z]+)", word.lower()).group()
        print last_syl
        if last_syl in suffdict:
            return suffdict[last_syl][0]
        elif last_syl[1 - len(last_syl):] in suffdict:
            return suffdict[last_syl[1 - len(last_syl):]][0]
        elif last_syl[-2:] == "'s" and last_syl[:-2] in suffdict:
            return suffdict[last_syl[:-2]][0].append('Z')
        elif last_syl[-1] == "s" and last_syl[:-1] in suffdict:
            return suffdict[last_syl[:-1]][0].append('Z')
        else:  # If not in cmudict or my cmusuffdict
            return False
    else:
        return False


def cmu_phonemes(word):
    # If in cmudict, just use cmudict
    if not word.lower() in d:
        return False
    else:
        return min(d[word.lower()], key=len)


hit = 0
miss = 0

for word, vals in d.iteritems():
    cmu = cmu_phonemes(word)
    suff = suffdict_phonemes(word)
    if cmu and suff and poetry.rhyme_from_phonemes(cmu, suff):
        print "hit: "
        print word
        hit += 1
    elif not cmu:
        print "Not in cmudict!"
    elif not suff:
        print "Not in suffdict!"
    else:
        print "miss: "
        print word
        miss += 1

print "hits: "
print hit
print "misses: "
print miss
print "Percent accuracy: "
print (hit / (hit + miss)) * 100

# Current results:
# hits:
# 98390
# misses:
# 24160
# Percent accuracy:
# 80.2855977152
