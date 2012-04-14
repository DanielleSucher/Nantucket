import poetry
import argparse

parser = argparse.ArgumentParser(description='Find accidental limericks in any text.')
parser.add_argument('--text',
                   help='the file you want to search for limericks in, ie "ulysses.txt"')
args = parser.parse_args()

tokens = poetry.tokenize(args.text)


def overflows_line(syllable_counter, current_sylct):
    ''' return true if the word would overflow the line '''

    # see what the new syllable count would be if we added this word
    new_sylct = syllable_counter + current_sylct

    # iterate through the syllable counts marking the end of each of the five
    # lines in a standard limerick. for each line, check if the old syllable
    # count has not exceeded that line and the new one has
    line_endings = [8, 16, 21, 26, 35]
    for count in line_endings:
      if syllable_counter < count and new_sylct > count:
        return True

    return False

def new_word_data(word):
    ''' return a dict with the syllable count and phonemes in the word '''
    return {"sylct": poetry.nsyl(word), "phonemes": poetry.phonemes(word)}

def check_rhyme(rhyme_scheme, line, phonemes):
    ''' rhyme_scheme: a dict of end rhymes for the current limerick, of the form
                        {'A': phoneme, 'B': phoneme}
        line:         position of line whose ending we are checking ('A' or 'B')
        phonemes:     the phoneme ending the current line, to check against rhyme_scheme
    '''
    if not line in rhyme_scheme:
        return False

    return poetry.rhyme_from_phonemes(rhyme_scheme[line], phonemes)

limericks = []
word_data = {}
i = 0
while i < len(tokens):
    if tokens[i] == '':
        tokens.remove('')
        continue
    start_word = tokens[i]
    if not start_word in word_data:
        word_data[start_word] = new_word_data(start_word)
        # Uses more space in exchange for getting more speed
    word_array = [start_word]
        # Holds the actual words of the potential limerick
    syllable_counter = word_data[start_word]['sylct']
    n = i + 1
    rhyme_scheme = {}  # Tracks the rhyme scheme
    while n < len(tokens):
        if tokens[n] == '':
            tokens.remove('')
            continue
        next_word = tokens[n]
        if not next_word in word_data:
            word_data[next_word] = new_word_data(next_word)
        sylct = word_data[next_word]['sylct']
        if overflows_line(syllable_counter, sylct):
            break  # break out if a word overflows the line
        word_array.append(next_word)
        syllable_counter += sylct
        phonemes = word_data[next_word]['phonemes']

        # abandon the current limerick-in-progress if we hit a word
        # with no phoneme data
        if not phonemes:
            break

        if syllable_counter == 8:
            rhyme_scheme['A'] = phonemes
            word_array.append("\n")
        elif syllable_counter == 16:
            word_array.append("\n")
            if not check_rhyme(rhyme_scheme, 'A', phonemes):
                break
        elif syllable_counter == 21:
            if phonemes == rhyme_scheme['A']:
                break
            rhyme_scheme['B'] = phonemes
            word_array.append("\n")
        elif syllable_counter == 26:
            word_array.append("\n")
            if not check_rhyme(rhyme_scheme, 'B', phonemes):
                break
        elif syllable_counter == 35:
            if check_rhyme(rhyme_scheme, 'A', phonemes):
                limericks.append(word_array)
            break
        n += 1
    i += 1

if limericks == []:
    print "Sorry, there were no limericks found in your text!"
else:
    for limerick in limericks:
        limerick = " ".join(limerick)
        print limerick
