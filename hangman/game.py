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
    if len(answer_word) == 0:
      raise InvalidWordException()
    elif len(character) > 1:
      raise InvalidGuessedLetterException()
    elif len(answer_word) != len(masked_word):
      raise InvalidWordException()
    else:
      answer_word = answer_word.lower()
      characters = list(answer_word)
      masked_word_list = list(masked_word)
      counter = 0
      for c in characters:
        character = character.lower()
        if c == character:
          masked_word_list[counter] = character
        counter = counter + 1
      return ''.join(masked_word_list)
    
    
def guess_letter(game, letter):
    pass
    if game['remaining_misses'] == 0 or game['answer_word'].lower() == game['masked_word'].lower():
      raise GameFinishedException
    if len(list(letter)) > 1:
      raise InvalidGuessedLetterException
    guesses = game['previous_guesses']
    remaining = game['remaining_misses']
    word = _uncover_word(game['answer_word'], game['masked_word'], letter)
    game['masked_word'] = word
    guesses.append(letter.lower())
    game['previous_guesses'] = guesses
      
    if letter.lower() in game['answer_word'].lower():
      game['remaining_misses'] = int(remaining)
    else:
      game['remaining_misses'] = int(remaining) - 1
      
    if game['remaining_misses'] == 0:
      raise GameLostException
    if word.lower() == game['answer_word'].lower():
      raise GameWonException
        
    return game
    


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
