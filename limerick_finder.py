import poetry


tokens = poetry.tokenize("knox.txt")


def not_haiku(maybe_nsyl, sylct):  # return true if the word would overflow the line
    if maybe_nsyl < 8 and sylct > 8 - maybe_nsyl:
        return True
    elif maybe_nsyl < 16 and sylct > 16 - maybe_nsyl:
        return True
    elif maybe_nsyl < 21 and sylct > 21 - maybe_nsyl:
        return True
    elif maybe_nsyl < 27 and sylct > 27 - maybe_nsyl:
        return True
    elif maybe_nsyl < 36 and sylct > 36 - maybe_nsyl:
        return True
    return False


limericks = []
maybe = []
maybe_nsyl = []
maybe_list = []
for i, w in enumerate(tokens):
    maybe.append([w])  # Holds the actual words of the potential limerick
    maybe_nsyl.append(poetry.nsyl(w))  # Syllable counter
    maybe_list.append(poetry.phonemes(w))  # List of lists of phonemes for each word
    n = i + 1
    give_up = False
    rhyme_scheme = {}  # Tracks the rhyme scheme
    while not give_up and n < len(tokens):
        print tokens[n]
        sylct = poetry.nsyl(tokens[n])
        give_up = not_haiku(maybe_nsyl[i], sylct)  # break out if a word overflows the line
        maybe[i].append(tokens[n])
        print maybe[i]
        maybe_nsyl[i] += sylct
        phonemes = poetry.phonemes(tokens[n])
        maybe_list[i].append(phonemes)
        if maybe_nsyl[i] == 8:
            rhyme_scheme['A'] = phonemes
            maybe[i].append("\n")
        elif maybe_nsyl[i] == 16:
            maybe[i].append("\n")
            if not poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes):
                give_up = True
        elif maybe_nsyl[i] == 21:
            rhyme_scheme['B'] = phonemes
            maybe[i].append("\n")
        elif maybe_nsyl[i] == 27:
            maybe[i].append("\n")
            if not poetry.rhyme_from_phonemes(rhyme_scheme['B'], phonemes):
                give_up = True
        elif maybe_nsyl[i] == 36:
            if poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes):
                limericks.append(maybe[i])
            give_up = True
        n += 1

for limerick in limericks:
    " ".join(limerick)
    print limerick
