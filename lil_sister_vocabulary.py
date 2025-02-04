
input = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
              'echolalia', 'encoder', 'biography']

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    # return vocab_words[0] + f'{vocab_words[0]} :: '.join(vocab_words[1:-1])
    # return vocab_words[0] + ' :: '.join(vocab_words[1:])
    return  vocab_words[0] + ' :: ' + ' :: '.join([vocab_words[0] + x  for x in vocab_words[1:]])

# print(make_word_groups(input))

word = 'heaviness'
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    

    if word[-5:] == 'iness':
        return word.replace('iness', 'y')
    else:
        return word.replace('ness', '')

# print(remove_suffix_ness(word))
# print(word[-5:])


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    return sentence.split()[index].replace('.', '') + 'en'

print(adjective_to_verb('I need to make that bright.', -1 ))