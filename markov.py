"""Generate markov text from text files."""


from random import choice
import sys
import twitter
import os

def open_and_read_file(args):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = ""
    for files in args:
        text1 = open(files).read()
        text += text1 
    
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
    counter = 0
    start = choice(chains.keys())
    while True:
        if start[0].istitle():
            words.extend(start[:])
            len_list = [len(item) + 1 for item in start]
            counter += sum(len_list)
            break
        else:
            start = choice(chains.keys())
    stop = None
    while counter <= 140:
        values = chains[tuple(words[-n:])]
        if words[-1][-1] in (".", "!", "?"):
            stop = len(words)
        if values is None:
            break
        else:
            chosen_value = choice(values)
            if counter + len(chosen_value) < 140:
                words.append(chosen_value)
                counter += len(chosen_value) + 1
            else:
                if stop:
                    words = words[:stop]
                break

    # your code goes here
    return " ".join(words)


def tweet(chains):
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # This will print info about credentials to make sure
    # they're correct
    # print api.VerifyCredentials()
    status = api.PostUpdate(chains)
    print status.text
    # Send a tweet
    while True:
        user_choice = raw_input("Enter t to tweet again, q to quit: ")
        if user_choice == "q":
            sys.exit()
        elif user_choice == "t":
            main()
            status = api.PostUpdate(tweetchain)
            print status.text
        else:
            print "Not a valid entry!"


def main():
    input_paths = sys.argv[1:]

    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_paths)

    # Get a Markov chain
    
    chains = make_chains(input_text, n)

    # Produce random text
    tweetchain = make_text(chains)

    tweet(tweetchain)

n = int(raw_input("How long would like your ngram? "))
main()

# def print_text(random_text):
#     """Makes word string less than 140 characters and ends with punctuation"""
#     while True:
#         if c <= 140 #and (random_text[-1] in (".", "!", "?", ",")):
#             return random_text
#             break
#         else:
#             random_text = make_text(chains)


