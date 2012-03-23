from __future__ import division
from curses.ascii import isdigit
from nltk.corpus import cmudict
d = cmudict.dict()


def nsyl(word):
    # return the max syllable count in the case of multiple pronunciations
    return max([len([y for y in x if isdigit(y[-1])]) for x in d[word.lower()]])
    # For example: d["concatenate".lower()] == [['K', 'AH0', 'N', 'K', 'AE1', 'T', 'AH0', 'N', 'EY2', 'T']]
    # This grabs each item where the last character is a digit (how cmudict represents vowel sounds), and counts them
    # Algorithm via http://runningwithdata.com/post/3576752158/w

print "concatenate:"
print nsyl("concatenate")


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

# Tests:
# print "do test and best rhyme?"
# print rhyme("test", "best")

# print "do store and rapport rhyme?"
# print rhyme("store", "rapport")
