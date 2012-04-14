#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import poetry
import argparse
import cgi

parser = argparse.ArgumentParser(description='Find accidental limericks in any text.')
parser.add_argument('--text',
                   help='the file you want to search for limericks in, ie "ulysses.txt"')
args = parser.parse_args()


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


def find_limericks(tokens, linebreak):
    limericks = []

    # Store the syllable count and phonemes for words we encounter
    # Uses more space in exchange for getting more speed
    word_data = {}

    i = 0
    while i < len(tokens):
        start_word = tokens[i]
        if not start_word in word_data:
            word_data[start_word] = new_word_data(start_word)

        # Holds the actual words of the potential limerick
        word_array = [start_word]

        syllable_counter = word_data[start_word]['sylct']
        n = i + 1
        rhyme_scheme = {}  # Tracks the rhyme scheme
        while n < len(tokens):
            next_word = tokens[n]
            if not next_word in word_data:
                word_data[next_word] = new_word_data(next_word)
            sylct = word_data[next_word]['sylct']

            # break out if a word overflows the line
            if overflows_line(syllable_counter, sylct):
                break

            word_array.append(next_word)
            syllable_counter += sylct
            phonemes = word_data[next_word]['phonemes']

            # abandon the current limerick-in-progress if we hit a word
            # with no phoneme data
            if not phonemes:
                break

            if syllable_counter == 8:
                rhyme_scheme['A'] = phonemes
                word_array.append(linebreak)
            elif syllable_counter == 16:
                word_array.append(linebreak)
                if not check_rhyme(rhyme_scheme, 'A', phonemes):
                    break
            elif syllable_counter == 21:
                if phonemes == rhyme_scheme['A']:
                    break
                rhyme_scheme['B'] = phonemes
                word_array.append(linebreak)
            elif syllable_counter == 26:
                word_array.append(linebreak)
                if not check_rhyme(rhyme_scheme, 'B', phonemes):
                    break
            elif syllable_counter == 35:
                if check_rhyme(rhyme_scheme, 'A', phonemes):
                    limericks.append(word_array)
                break
            n += 1
        i += 1
    return limericks


# handle web version
if cgi.FieldStorage():
    url = cgi.FieldStorage()['url'].value
    if url[-4:] != ".txt":
        print "Content-type: text/html\n\n"
        print "Sorry, Nantucket only works with links to .txt files at the moment!<br><br>"
    else:
        tokens = poetry.tokenize_from_url(url)
        limericks = find_limericks(tokens, "<br>")
        print "Content-type: text/html\n\n"
        if limericks == []:
            print "Sorry, there were no limericks found in your text!<br><br>"
        else:
            for limerick in limericks:
                limerick = " ".join(limerick)
                print limerick
                print "<br><br>"
    print "<a href='/nantucket/nantucket.html'>Return to Nantucket to find more limericks!</a>"

# handle command line version
if args:
    tokens = poetry.tokenize(args.text)
    limericks = find_limericks(tokens, "\n")
    if limericks == []:
        print "Sorry, there were no limericks found in your text!"
    else:
        for limerick in limericks:
            limerick = " ".join(limerick)
            print limerick
