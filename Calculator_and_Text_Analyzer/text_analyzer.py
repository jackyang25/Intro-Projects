# Author: Jack Yang

####### DO NOT EDIT FUNCTIONS BELOW ########

def character_is_digit(char):
    """Indicates whether the value referenced by char parameter
    is a digit character

    :param char: character to check
    :return: True when char is a digit character, False otherwise

    >>> test_char = 'b'
    >>> character_is_digit(test_char)
    False
    >>> test_char = '2'
    >>> character_is_digit(test_char)
    True
    """

    return char.isdigit()


def character_is_letter(char):
    """Indicates whether the value referenced by char parameter
    is a letter

    :param char: character to check
    :return: True when char is a letter, False otherwise

    >>> test_char = 'b'
    >>> character_is_letter(test_char)
    True
    >>> test_char = '2'
    >>> character_is_letter(test_char)
    False
    """

    return char.isalpha()


def character_is_whitespace(char):
    """Indicates whether the value referenced by char parameter
    is a whitespace character (' ', '\n', '\t')
    :param char: character to check
    :return: True when char is space character, False otherwise
    >>> test_char = ' '
    >>> character_is_whitespace(test_char)
    True
    >>> test_char = '#'
    >>> character_is_whitespace(test_char)
    False
    >>> test_char = '\n'
    >>> character_is_whitespace(test_char)
    True
    >>> test_char = '\t'
    >>> character_is_whitespace(test_char)
    True
    """

    if char == " ":
        return True

    if char == "\n":
        return True

    if char == '\t':
        return True


def character_ends_sentence(char):
    """Indicates whether the value referenced by char parameter
    is a period, question mark, or exclamation point
    :param char: character to check
    :return: True when char ends sentence, False otherwise
    >>> test_char = 'k'
    >>> character_ends_sentence(test_char)
    False
    >>> test_char = '.'
    >>> character_ends_sentence(test_char)
    True
    >>> test_char = '?'
    >>> character_ends_sentence(test_char)
    True
    >>> test_char = '!'
    >>> character_ends_sentence(test_char)
    True
    """

    if char == ".":
        return True

    if char == "?":
        return True

    if char == "!":
        return True


def print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences):
    """Prints the number of total characters, spaces, digits, letters,
    and sentences identified in the text being analyzed.
    :param num_chars: number of total characters in text
    :param num_spaces: number of spaces in text
    :param num_digits: number of digits in text
    :param num_letters: number of letters in text
    :param num_sentences: number of sentences in text
    :return: None
    >>> num_chars = 234
    >>> num_spaces = 14
    >>> num_digits = 16
    >>> num_letters = 201
    >>> num_sentences = 21
    >>> print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)
    <BLANKLINE>
    Count of characters: 234
    Count of spaces: 14
    Count of digits: 16
    Count of letters: 201
    Count of sentences: 21
    <BLANKLINE>
    """

    print()
    print("Count of characters:", num_chars)
    print("Count of spaces:", num_spaces)
    print("Count of digits", num_digits)
    print("Count of letters", num_letters)
    print("Count of sentences", num_sentences)
    print()


def analyze_text():
    """Calls the functions to compute the number of total characters,
    spaces, digits, letters, and sentences in user-supplied text and to
    output the final counts when text input by user.
    :return: True when text provided, False when no text provided
    """

    user_text = input("Please enter text to analyze (press ENTER/return without text to exit): ")

    num_spaces = 0
    num_digits = 0
    num_letters = 0
    num_sentences = 0

    if user_text == "":
        print()
        print('Goodbye.')

        return False

    if user_text:

        for x in range(len(user_text)):
            char = user_text[x]
            num_chars = len(user_text)

            if character_is_whitespace(char) is True:
                num_spaces = num_spaces + 1

            elif character_is_letter(char) is True:
                num_letters = num_letters + 1

            elif character_ends_sentence(char) is True:
                num_sentences = num_sentences + 1

            elif character_is_digit(char) is True:
                num_digits = num_digits + 1

        print_results(num_chars, num_spaces, num_digits, num_letters, num_sentences)

        return True


def run_text_analyzer():
    """Runs the Text Analyzer as a repeated sequence of
     prompting the user for input text and outputting the
     character counts computed from the input
     :return: None
    """

    print("Welcome to the Text Analyzer!")
    print()

    while analyze_text() == True:
        analyze_text()

####### DO NOT EDIT FUNCTIONS ABOVE ########

def main():
    """Runs a program for analyzing character counts from
    input text
    """

    run_text_analyzer()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests

    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)
    # print("\nRunning program...\n")

    main()
