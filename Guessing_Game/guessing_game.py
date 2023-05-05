# Author: Jack Yang

####### DO NOT EDIT CODE BELOW (changing MAX_MISSES is ok) ########

import random
import sys

MAX_MISSES = 5
BORDER_LENGTH = 30
SINGLE_CHAR_LENGTH = 1

####### DO NOT EDIT CODE ABOVE (changing MAX_MISSES is ok) ########

def display_game_state(chars, misses):
    """
    Displays the current state of the game: the list of characters to display
    and the list of misses.
    """

    print()
    print('=' * BORDER_LENGTH)
    print()

    print("Word:\t{}\n".format(space_chars(chars)))
    print("Misses:\t{}\n".format("".join(misses)))


def blank_chars(word):
    """Returns a list of underscore characters with the same length as word.
    :param word: target word as a string
    :return: a list of underscore characters ('_')
    >>> blank_chars("happiness")
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    """

    word_list = list(word)
    for char in range(0, len(word_list)):
        word_list.append("_")
        word_list.pop(0)

    return word_list


def space_chars(chars):
    """Returns a string with the characters in chars list separated by spaces.
    :param chars: a list of characters
    :return: a string containing characters in chars with intervening spaces
    >>> space_chars(['h', '_', 'p', 'p', '_', 'n', '_', '_', '_'])
    'h _ p p _ n _ _ _'
    """

    return " ".join(chars)


def get_guess():
    """Prompts the user for a guess to check for the game's current word. When the user
    enters input other than a single character, the function prompts the user again
    for a guess. Only when the user enters a single character will the prompt for
    a guess stop being displayed. The function returns the single-character guess
    entered by the user.
    :return guess: a single character guessed by user
    """

    x = 0
    while x == 0:
        guess = input("Guess:\t")
        if len(guess) is SINGLE_CHAR_LENGTH and guess.isalpha():
            x += 1

    return guess.lower()


def check_guess(word, guess):
    """Returns a list of positions where guess is present in word.
    An empty list should be returned when guess is not a single
    character or when guess is not present in word.
    :param word: target word as a string
    :param guess: a single character guessed by user
    :return positions: list of integer positions
    """

    list = []
    x = -1

    for i in word:
        x += 1
        if i == guess:
            list.append(x)
    else:
        return list


def update_chars(chars, guess, positions):
    """Updates the list of characters, chars, so that the characters
    at the index values in the positions list are updated to the
    character guess.
    :param chars: a list of characters
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """

    for i in positions:
        chars[i] = guess


def add_to_misses(misses, guess):
    """Adds the character guess to the misses list.
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :return: None
    """

    misses += guess


def update_state(chars, misses, guess, positions):
    """Updates the state of the game based on user's guess. Calls the function update_chars() when
    the positions list is not empty to reveal the indices where the character guess is present. Calls the
    function add_to_misses() when the positions list is empty to add guess to the misses list.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :param guess: a single character guessed by user
    :param positions: list of integer positions
    :return: None
    """

    if positions != []:
        update_chars(chars, guess, positions)
    else:
        add_to_misses(misses, guess)


def is_round_complete(chars, misses):
    """Indicates whether or not a round has ended. This function returns True
    when the user has successfully guessed the target word or exceeds the
    number of allowed misses. Otherwise, the function returns False,
    indicating that the round is not complete. A message revealing the
    user's success or failure guessing the target word is output by this
    function when the round is complete.
    :param chars: a list of characters
    :param misses: list of guesses not present in target word
    :return status: True when round is finished, False otherwise
    """

    if "_" not in chars:
        print('')
        print('YOU GOT IT!')
        return True

    elif len(misses) > MAX_MISSES:
        print('')
        print("SORRY! NO GUESSES LEFT.")
        return True

    else:
        return False


def read_words(filepath):
    """Opens a file of word located at filepath, reads the file of words line by line,
    and adds each word from the file to a list. The list is returned by the
    function
    :param filepath: path to input file of words (one per line)
    :return word_list: list of strings contained in input file
    """

    file_object = open(filepath, 'r')
    list = []
    for line in file_object:
        x = line.strip()
        list.append(x)
    file_object.close()

    return list


def get_word(words):
    """Selects a single word randomly from words list and returns it.
    :param words: list of strings
    :return word: string from words list
    """

    num = random.randrange(0, len(words))

    return words[num]


def is_game_complete():
    """Prompts the user with "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'.
    :return response: boolean representing game completion status
    """

    response = ""

    while response != "n" or response != "y":
        response = input("Play again (Y/N)?").lower()
        if response == "n":
            return True
        if response == "y":
            return False
        else:
            response = input("Play again (Y/N)?").lower()


def run_guessing_game(words_filepath):
    """Controls running The Guessing Game. This includes parsing
    the words file and executing multiple rounds of the game.
    :param words_filepath: the location of the file of words for the game
    :return: None
    """

    try:
        words_list = read_words(words_filepath)
        print("Welcome to The Guessing Game!")
        complete = False
        while complete is False:
            misses = []
            random_word = get_word(words_list)
            blank = blank_chars(random_word)
            display_game_state(blank, misses)

            guess = get_guess()
            positions = check_guess(random_word, guess)
            update_state(blank, misses, guess, positions)
            complete = is_round_complete(blank, misses)

            while complete == False:
                display_game_state(blank, misses)
                guess = get_guess()
                positions = check_guess(random_word, guess)

                update_state(blank, misses, guess, positions)
                complete = is_round_complete(blank, misses)

            display_game_state(random_word, misses)
            complete = is_game_complete()
        print()
        print("Goodbye.")
    except FileNotFoundError:
        print("The provided file location is not valid. Please enter a valid path to a file.")


def main():

    ########## DO NOT EDIT ASSIGNMENT STATEMENT BELOW #########

    filepath = sys.argv[-1]

    ########## DO NOT EDIT ASSIGNMENT STATEMENT ABOVE #########

    # calls run_guessing_game() with filepath as argument

    run_guessing_game(filepath)


if __name__ == '__main__':
    main()
