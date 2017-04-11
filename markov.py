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


def make_chains(text_string):
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
    for i in range(len(text) - 2):
        if tuple([text[i], text[i+1]]) in chains:
            chains[tuple([text[i], text[i+1]])].append(text[i+2])
        else:
            chains[tuple([text[i], text[i+1]])] = [text[i+2]]
    chains[tuple([text[-2], text[-1]])] = None

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    start = choice(chains.keys())
    while True:
        if start[0].istitle():
            words.extend([start[0], start[1]])
            break
        else:
            start = choice(chains.keys())

    while True:
        values = chains[tuple([words[-2], words[-1]])]
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
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
