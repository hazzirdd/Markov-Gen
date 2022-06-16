from cgitb import text
from hashlib import new
from random import choice
import random


def open_and_read_file(file_path):

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
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
    
def main(input_text):
    # input_path = 'green-eggs.txt'

    # Open the file and turn it into one long string
    # input_text = open_and_read_file(input_path)

    # Get a Markov chain
    chains = make_chains(input_text)

    # Produce random text
    random_text = make_text(chains)

    return random_text
