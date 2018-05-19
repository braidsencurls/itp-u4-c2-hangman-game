from .exceptions import *
from random import randint

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Python', 'Hello World', 'Women Who Code']


def _get_random_word(list_of_words):
    pass
    if len(list_of_words) != 0:
       random_index = randint(0, len(list_of_words)-1)
    else:
        raise InvalidListOfWordsException()
    return list_of_words[random_index];


def _mask_word(word):
    pass
    if word != '':
        letters_of_word = list(word)
        for letter in letters_of_word:
            word = word.replace(letter, '*')
        return word
    else:
        raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    pass


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
