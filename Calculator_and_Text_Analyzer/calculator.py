# Author: Jack Yang

def print_menu():

    print()
    print("1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")


def do_calculation(menu_selection_input):

    if menu_selection_input == 'q':
        print()
        print('Goodbye')

    elif menu_selection_input == "1":
        do_addition()

    elif menu_selection_input == "2":
        do_subtraction()

    elif menu_selection_input == "3":
        do_multiplication()

    elif menu_selection_input == "4":
        do_division()

    else:
        print()
        print('That was not a valid choice. Try again.')


def run_calculator():

    print("Welcome to my calculator!")

    menu_selection_input = 0

    while menu_selection_input != 'q':
        print_menu()
        menu_selection_input = input("Please enter an option (1-4) or 'q' to quit: ")
        do_calculation(menu_selection_input)


def do_addition():
    """Informs user that addition was chosen, sums two
     numbers input by the user, and outputs the result.
     :return: None
     """

    print()
    print("You have chosen the addition operation.")

    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))
    number_sum = number_1 + number_2

    print("The result of the addition of the two numbers is", number_sum, ".")


def do_subtraction():
    """Informs user that subtraction was chosen, calculates
    the difference between two numbers input by the user, and
    outputs the result.
    :return: None
    """

    print()
    print("You have chosen the subtraction operation.")

    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))
    number_sub = number_1 - number_2

    print("The result of the subtraction of the two numbers is", number_sub, ".")


def do_multiplication():
    """Informs user that multiplication was chosen, multiplies two
    numbers input by the user, and outputs the result.
    :return: None
    """
    print()
    print("You have chosen the multiplication operation.")

    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))
    number_product = number_1 * number_2

    print("The result of the multiplication of the two numbers is", number_product, ".")


def do_division():
    """Informs user that division was chosen, divides two
    numbers input by the user, and outputs the result.
    :return: None
    """

    print()
    print("You have chosen the division operation.")

    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))
    number_div = number_1 / number_2

    print("The result of the division of the two numbers is", number_div, ".")


def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """

    run_calculator()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests

    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)
    # print("\nRunning program...\n")

    main()
