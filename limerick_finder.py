import poetry

tokens = []
poetry.tokenize("genesis.txt", tokens)


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


maybe = []
maybe_list = []
maybe_nsyl = 0
for i, w in enumerate(tokens):
    maybe.append(w)  # Holds the actual words of the potential limerick
    maybe_nsyl += poetry.nsyl(w)  # Syllable counter
    maybe_list.append(poetry.phonemes(w))  # List of lists of phonemes for each word
    n = i + 1
    give_up = False
    rhyme_scheme = {}  # Tracks the rhyme scheme
    while not give_up:
        sylct = poetry.nsyl(tokens[n])
        give_up = not_haiku(maybe_nsyl, sylct)  # break out if a word overflows the line
        maybe.append(tokens[n])
        maybe_nsyl += sylct
        phonemes = poetry.phonemes(tokens[n])
        maybe_list.append(phonemes)
        n += 1
        if maybe_nsyl == 8:
            rhyme_scheme['A'] = tokens[n]
            maybe.append("\n")
            break
        elif maybe_nsyl == 16:
            if poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes):
                break
            else:
                give_up = True
        elif maybe_nsyl == 21:
            rhyme_scheme['B'] = tokens[n]
            maybe.append("\n")
            break
        elif maybe_nsyl == 27:
            if poetry.rhyme_from_phonemes(rhyme_scheme['B'], phonemes):
                break
            else:
                give_up = True
        elif maybe_nsyl == 36:
            if poetry.rhyme_from_phonemes(rhyme_scheme['A'], phonemes):
                break  # Nope, save the damn haiku
            else:
                give_up = True
