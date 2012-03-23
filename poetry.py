from __future__ import division
import re
from curses.ascii import isdigit
from nltk.corpus import cmudict
d = cmudict.dict()


def nsyl(word):
    # return the max syllable count in the case of multiple pronunciations
    return max([len([y for y in x if isdigit(y[-1])]) for x in d[word.lower()]])
    # For example: d["concatenate".lower()] == [['K', 'AH0', 'N', 'K', 'AE1', 'T', 'AH0', 'N', 'EY2', 'T']]
    # This grabs each item where the last character is a digit (how cmudict represents vowel sounds), and counts them
    # Algorithm via http://runningwithdata.com/post/3576752158/w


# Still needs code for fallback when a word isn't found in cmudict
def rhyme(word1, word2):
    reverse_word1 = max(d[word1.lower()], key=len)
    reverse_word1.reverse()
    reverse_word2 = max(d[word2.lower()], key=len)
    reverse_word2.reverse()
    for i, v in enumerate(reverse_word1):
        if isdigit(v[-1]):
            if reverse_word1[:i] == reverse_word2[:i]:
                return True
    return False


def tokenize(file_path, array):
    with open(file_path) as f:
        data = f.read()
        data = re.sub("[^a-zA-Z\s-]", '', data)
        data = re.sub("\s+", " ", data)
        words = re.split("\s|-", data)
        array += words
    if array[0] == '': del array[0]
    if array[-1] == '': del array[-1]

# Tests:
# print "concatenate:"
# print nsyl("concatenate")

# print "do test and best rhyme?"
# print rhyme("test", "best")

# print "do store and rapport rhyme?"
# print rhyme("store", "rapport")
