from __future__ import division
import re
import urllib2
from curses.ascii import isdigit
from nltk.corpus import cmudict
d = cmudict.dict()
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import *
suffdict = LazyCorpusLoader(
    'cmusuffdict', CMUDictCorpusReader, ['cmusuffdict'])
suffdict = suffdict.dict()

def try_syllable(syl):
    ''' helper function for phonemes()
    Tests if syl is in suffdict. If not, removes the first letter
    and then the first two letters, checking each time
    '''
    if syl in suffdict:
        return suffdict[syl][0]
    # else try without the first letter
    elif syl[1:] in suffdict:
        return suffdict[syl[1:]][0]
    # else try without the first 2 letters
    elif syl[2:] in suffdict:
        return suffdict[syl[2:]][0]
    # else return None, which the calling function should check for
    else:
        return None

def phonemes(word):
    word = word.lower()
    # If in cmudict, just use cmudict
    if word in d:
        return min(d[word], key=len)

    # If not, try to use my cmu-based last syllable dictionary

    # if we cannot detect the last syllable, give up
    syl_re = re.compile("([bcdfghjklmnpqrstvwxz]{1,2}[aeiouy]+[bcdfghjklmnpqrstvwxz]*(e|ed)?('[a-z]{1,2})?)(?![a-zA-Z]+)")
    if not syl_re.search(word):
        return False

    last_syl = syl_re.search(word).group()

    # now try the last syllable against cmusuffdict
    p = try_syllable(last_syl)
    if p:
        return p
    # else try without the last 2 letters, if it ends in 's
    elif last_syl[-2:] == "'s":
        p = try_syllable(last_syl[:-2])
        if p:
            return p.append('Z')
        else:
            return False
    # else try without the last letter, if it ends in s
    elif last_syl[-1] == "s":
        p = try_syllable(last_syl[:-1])
        if p:
            return p.append('Z')
        else:
            return False
    else:  # If not in cmudict or my cmusuffdict
        return False


def approx_nsyl(word):
    digraphs = {"ai", "au", "ay", "ea", "ee", "ei", "ey", "oa", "oe", "oi", "oo", "ou", "oy", "ua", "ue", "ui"}
    # Ambiguous, currently split: ie, io
    # Ambiguous, currently kept together: ui
    count = 0
    array = re.split("[^aeiouy]+", word.lower())
    for i, v in enumerate(array):
        if len(v) > 1 and v not in digraphs:
            count += 1
        if v == '':
            del array[i]
    count += len(array)
    if re.search("(?<=\w)(ion|ious|(?<!t)ed|es|[^lr]e)(?![a-z']+)", word.lower()):
        count -= 1
    if re.search("'ve|n't", word.lower()):
        count += 1
    return count


def nsyl(word):
    # return the min syllable count in the case of multiple pronunciations
    if not word.lower() in d:
        return approx_nsyl(word)
    return min([len([y for y in x if isdigit(y[-1])]) for x in d[word.lower()]])
    # For example: d["concatenate".lower()] == [['K', 'AH0', 'N', 'K', 'AE1', 'T', 'AH0', 'N', 'EY2', 'T']]
    # Oh, and those numbers are actually stress/inflection (0: no stress, 1: primary stress, 2: secondary stress)
    # This grabs each item where the last character is a digit (how cmudict represents vowel sounds), and counts them


# Ignores stress for now, while I'm not taking meter into account
def rhyme_from_phonemes(list1, list2):
    i = -1
    while i >= 0 - len(list1):
        if isdigit(list1[i][-1]):
            if i >= 0 - len(list2) and list1[i][:-1] == list2[i][:-1] and (i == -1 or list1[i + 1:] == list2[i + 1:]):
                return True
            else:
                return False
        i -= 1


def rhyme(word1, word2):
    list1 = min(d[word1.lower()], key=len)
    list2 = min(d[word2.lower()], key=len)
    return rhyme_from_phonemes(list1, list2)


def tokenize_text(text):
    text = re.sub("[^a-zA-Z\s'-]", '', text)
    text = re.sub("'(?![a-z]{1,2})", '', text)
    tokens = re.split("\s+|-", text)
    # remove empty tokens
    tokens = filter(None, tokens)
    return tokens

def tokenize(file_path):
    with open(file_path) as f:
        data = f.read().strip()
    return tokenize_text(data)

def tokenize_from_url(url):
    data = urllib2.urlopen(url).read().strip()
    return tokenize_text(data)

# Thinking about meter:
# In "there once" [was a man from Nantucket], I'd want to see that "there" is unstressed, and "once" is stressed
# But cmudict sees the single vowel in each of them as 1 (primary stress), because it looks at each word in isolation
# Maybe for now just assume than monosyllabic words are flexible, and use cmudict for stress on polysyllabic words?
