"""Generate Markov text from text files."""

from cgitb import text
from hashlib import new
from random import choice
import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        my_tuple = (words[i], words[i + 1])
        third_word = words[i + 2]

        if my_tuple in chains:
            chains[my_tuple].append(third_word)
        else:
            third_word_list = []
            third_word_list.append(third_word)

            chains[my_tuple] = third_word_list

    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    original_pair = list(chains.keys())[0]
    words.append(original_pair[0])
    words.append(original_pair[1])

    count = 0
    while count < 1000:
        last_pair = (f'{words[-2]}', f'{words[-1]}')
        if last_pair in chains:
            rand_value = random.choice(list(chains[(last_pair)]))
            words.append(rand_value)
            count += 1
        else:
            break

    return ' '.join(words)
    

input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
