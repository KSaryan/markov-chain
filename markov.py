"""Generate markov text from text files."""


from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text = open(file_path).read()

    return text


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

     # your code goes here
    text = text_string.split()
    for i in range(len(text) - n):
        seq = []
        indexes = i
        while len(seq) < n:
            seq.append(text[indexes])
            indexes += 1
        tupled = tuple(seq)
        chains.setdefault(tupled, [])
        chains[tupled].append(text[i+n])
        # if tuple(seq) in chains:
        #     chains[tuple(seq)].append(text[i+n])
        # else:
        #     chains[tuple(seq)] = [text[i+n]]
    chains[tuple(text[-n:])] = None

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    start = choice(chains.keys())
    while True:
        if start[0].istitle():
            words.extend(start[:n])
            break
        else:
            start = choice(chains.keys())

    while True:
        values = chains[tuple(words[-n:])]
        if words[-1][-1] in (".", "!", "?"):
            break
        if values is None:
            break
        else:
            words.append(choice(values))


    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
n = int(raw_input("How long would like your ngram? "))
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)

print random_text
