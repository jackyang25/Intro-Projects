# Author: Jack Yang

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16

####### DO NOT EDIT ABOVE ########

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """

    return random.choice(CARD_LABELS)


def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)
    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """

    if card_label == "A":
        return ACE_VALUE
    if (card_label == "J") or (card_label == "Q") or (card_label == "K"):
        return FACE_CARD_VALUE
    else:
        return int(card_label)


def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """
    draw_1 = deal_card()
    draw_2 = deal_card()
    print("Player drew", draw_1, "and", draw_2 + ".")
    print(f"Player's total is {get_card_value(draw_1) + get_card_value(draw_2)}.")
    print("")

    initial_total = get_card_value(draw_1) + get_card_value(draw_2)

    user_input = input("Hit (h) or Stay (s)?")
    print("")

    x = 0

    while x == 0 and initial_total < BLACKJACK:

        if user_input == "h":

            player_draw_another = deal_card()
            initial_total += get_card_value(player_draw_another)

            print(f'Player drew {player_draw_another}.')
            print(f"Player's total is {initial_total}.")
            print("")
            if initial_total < BLACKJACK:
                user_input = input("Hit (h) or Stay (s)?")
                print("")

        elif initial_total >= BLACKJACK:
            x += 1

        elif user_input == "s":
            x += 1

        else:
            user_input = input("Hit (h) or Stay (s)?")
            print("")

    return initial_total


def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total
    :return: the total value of the cards dealt
    """
    draw_1 = deal_card()
    draw_2 = deal_card()
    print("The dealer has", draw_1, "and", draw_2 + ".")
    print(f"Dealer's total is {get_card_value(draw_1) + get_card_value(draw_2)}.")

    initial_total = get_card_value(draw_1) + get_card_value(draw_2)

    while initial_total <= DEALER_THRESHOLD:
        print("")
        dealer_draw_another = deal_card()
        print(f'Dealer drew {dealer_draw_another}.')
        initial_total += get_card_value(dealer_draw_another)
        print(f"Dealer's total is {initial_total}.")

    print("")
    return initial_total


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """

    if dealer_total == BLACKJACK:
        print("YOU LOSE!")
        print("")

    elif player_total == BLACKJACK:
        print("YOU WIN!")
        print("")

    elif player_total > BLACKJACK:
        print("YOU LOSE!")
        print("")

    elif dealer_total > BLACKJACK and player_total <= BLACKJACK:
        print("YOU WIN!")
        print("")

    elif player_total > dealer_total:
        print("YOU WIN!")
        print("")

    else:
        print("YOU LOSE!")
        print("")


def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome
    :return: None
    """

    print("Let's Play Blackjack!")
    print("")

    x = 0
    while x == 0:
        p = deal_cards_to_player()

        if p > BLACKJACK:
            determine_outcome(p, 0)

        else:
            d = deal_cards_to_dealer()
            determine_outcome(p, d)

        new_game = input("Play again (Y/N)?")
        print("")

        while new_game != "Y" and new_game != "N":
            new_game = input("Play again (Y/N)?")
            print("")

        if new_game == "Y":
            pass
        if new_game == "N":
            x += 1
            print("Goodbye.")


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """
    play_blackjack()

####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    # Remove comments for next 4 lines to run doctests

    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)
    # print("\nRunning program...\n")

    main()
