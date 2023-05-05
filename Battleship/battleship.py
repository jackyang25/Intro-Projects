# Author: Jack Yang

import random

### DO NOT EDIT BELOW (with the exception of MAX_MISSES) ###

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
        random.choice(
            range(
                ord(MIN_ROW_LABEL),
                ord(MIN_ROW_LABEL) + NUM_ROWS
            )
        )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return row_choice, col_choice


def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_over = False

    while not game_over:

        game = Game()
        game.display_board()

        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()

        game_over = end_program()

    print("Goodbye.")

### DO NOT EDIT ABOVE (with the exception of MAX_MISSES) ###

class Ship:

    def __init__(self, name, start_position, orientation):
        """Creates a new ship with the given name, placed at start_position in the
        provided orientation. The number of positions occupied by the ship is determined
        by looking up the name in the SHIP_SIZE dictionary.

        :param name: the name of the ship
        :param start_position: tuple representing the starting position of ship on the board
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return: None
        """

        self.name = name
        self.sunk = False
        self.positions = {}
        ship_length = SHIP_SIZES[name]

        # number (x, number)
        column = start_position[COL_IDX]
        # letter (letter, x)
        row = start_position[ROW_IDX]

        if orientation is HORIZONTAL:
            for i in range(0, ship_length):
                column = start_position[COL_IDX]
                column = column + i
                # Creates position and checks if ship is sunk (boolean)
                self.positions[row, column] = False

        if orientation is VERTICAL:
            # iterates number of times depending on ship length
            for i in range(0, ship_length):
                # iterating the positions
                row_num = ord(row)
                row_num = row_num + i
                row_letter = chr(row_num)
                self.positions[row_letter, column] = False


class Game:

    ########## DO NOT EDIT #########

    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]

    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    ########## DO NOT EDIT #########

    def __init__(self, max_misses=MAX_MISSES):
        """ Creates a new game with max_misses possible missed guesses.
        The board is initialized in this function and ships are randomly
        placed on the board.

        :param max_misses: maximum number of misses allowed before game ends
        """

        self.ships = []
        self.guesses = []

        self.board = {}
        self.max_misses = MAX_MISSES

        self.initialize_board()
        self.create_and_place_ships()

    def initialize_board(self):
        """Sets the board to it's initial state with each position occupied by
        a period ('.') string.

        :return: None
        """

        for i in range(ord(MIN_ROW_LABEL), ord(MAX_ROW_LABEL) + 1):
            self.board[chr(i)] = [BLANK_CHAR, BLANK_CHAR, BLANK_CHAR, BLANK_CHAR, BLANK_CHAR, BLANK_CHAR, BLANK_CHAR,
                                  BLANK_CHAR, BLANK_CHAR, BLANK_CHAR]

    def in_bounds(self, start_position, ship_size, orientation):
        """Checks that a ship requiring ship_size positions can be placed at start position.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement inside board boundary, False otherwise
        """

        row_ascii = ord(start_position[ROW_IDX])

        # checks if vertical placement is in bound
        if orientation == VERTICAL:
            end_point = (row_ascii + ship_size, start_position[COL_IDX])
            if 65 <= end_point[ROW_IDX] <= 74:
                return True
            else:
                return False

        # checks if horizontal placement is in bound
        else:
            end_point = (start_position[ROW_IDX], start_position[COL_IDX] + ship_size)
            if 0 <= end_point[COL_IDX] <= 9:
                return True
            else:
                return False

    def overlaps_ship(self, start_position, ship_size, orientation):
        """Checks for overlap between previously placed ships and a potential new ship
        placement requiring ship_size positions beginning at start_position in the
        given orientation.

        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement overlaps previously placed ship, False otherwise
        """

        ship_pos = []

        if orientation == HORIZONTAL:
            # iterates number of times depending on ship length
            for i in range(ship_size):
                # adds horizontal coordinates to ship_pos list
                ship_pos.append((start_position[0], start_position[1] + i))
        else:
            # else is to check for vertical orientation
            for i in range(ship_size):
                # adds vertical coordinates to ship_pos list
                ship_pos.append((chr(ord(start_position[0]) + i), start_position[1]))

        # iterates number of times across ship objects
        for ship in self.ships:
            # iterates number of times across ship positions in dict
            for pos in ship.positions:
                # checks if position is in ship_pos, returns true when when it overlaps
                if pos in ship_pos:
                    return True

        # Skips to return statement if there is no overlap
        return False

    def place_ship(self, start_position, ship_size):
        """Determines if placement is possible for ship requiring ship_size positions placed at
        start_position. Returns the orientation where placement is possible or None if no placement
        in either orientation is possible.
        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :return orientation: 'h' if horizontal placement possible, 'v' if vertical placement possible,
            None if no placement possible
        """

        if self.in_bounds(start_position, ship_size, HORIZONTAL) is True and self.overlaps_ship(start_position,
                                                                                                ship_size,
                                                                                                HORIZONTAL) is False:
            return HORIZONTAL
        if self.in_bounds(start_position, ship_size, VERTICAL) is True and self.overlaps_ship(start_position, ship_size,
                                                                                              VERTICAL) is False:
            return VERTICAL

    def create_and_place_ships(self):
        """Instantiates ship objects with valid board placements.
        :return: None
        """

        for i in self._ship_types:
            place = None
            while place != VERTICAL and place != HORIZONTAL:
                random_pos = get_random_position()
                place = self.place_ship(random_pos, SHIP_SIZES[i])
            new_ship = Ship(i, random_pos, place)
            self.ships.append(new_ship)

    def get_guess(self):
        """Prompts the user for a row and column to attack. The
        return value is a board position in (row, column) format
        :return position: a board position as a (row, column) tuple
        """

        row = "Z"
        column = "Z"

        while (len(row) != 1) or (ord(row) < 65) or (ord(row) > 74):
            row = input("Enter a row: ")

        while (column.isdigit() != True) or (int(column) < 0) or (int(column) > 9):
            column = input("Enter a column: ")

        return row, int(column)

    def check_guess(self, position):
        """Checks whether or not position is occupied by a ship. A hit is
        registered when position occupied by a ship and position not hit
        previously. A miss occurs otherwise.
        :param position: a (row,column) tuple guessed by user
        :return: guess_status: True when guess results in hit, False when guess results in miss
        """

        for ship in self.ships:
            if position in ship.positions:

                if ship.positions[position]:
                    return False

                ship.positions[position] = True

                for key in ship.positions:
                    if ship.positions[key] is False:
                        return True

                print(f'You sunk the {ship.name}!.')
                ship.sunk = True
                return True

        return False

    def update_game(self, guess_status, position):
        """Updates the game by modifying the board with a hit or miss
        symbol based on guess_status of position.

        :param guess_status: True when position is a hit, False otherwise
        :param position:  a (row,column) tuple guessed by user
        :return: None
        """

        # When position is hit
        if guess_status is True:
            self.board[position[0]][position[1]] = HIT_CHAR
        # Other two miss conditions
        else:

            # When the position is already hit previously and hit again
            if self.board[position[0]][position[1]] == HIT_CHAR:
                self.guesses.append(position)

            # When the position is missed
            else:
                self.board[position[0]][position[1]] = MISS_CHAR
                self.guesses.append(position)

    def is_complete(self):
        """Checks to see if a Battleship game has ended. Returns True when the game is complete
        with a message indicating whether the game ended due to successfully sinking all ships
        or reaching the maximum number of guesses. Returns False when the game is not
        complete.
        :return: True on game completion, False otherwise
        """

        # First checks if the user exceeds the amount of guesses made
        if len(self.guesses) >= self.max_misses:
            print("SORRY! NO GUESSES LEFT.")
            return True

        # By default, the game condition all_sunk will always be true
        # Boolean value will change depending on the iteration below, which looks for a standing ship
        all_sunk = True

        # Iterates through ships for at least 1 standing ship (if found, all_sunk will change to False)
        for ship in self.ships:
            if not ship.sunk:
                all_sunk = False

        # Win condition
        if all_sunk is True:
            print("YOU WIN!")

        return all_sunk


def end_program():
    """Prompts the user with "Play again (Y/N)?" The question is repeated
    until the user enters a valid response (Y/y/N/n). The function returns
    False if the user enters 'Y' or 'y' and returns True if the user enters
    'N' or 'n'.

    :return response: boolean indicating whether to end the program
    """

    player_input = ""

    while player_input != "Y" and player_input != "N":
        player_input = input("Play again (Y/N)?").upper()

        if player_input == "N":
            return True

        if player_input == "Y":
            return False


def main():
    """Executes one or more games of Battleship."""

    # new_game = Game()
    # new_game.update_game(True,("C",5))

    play_battleship()


if __name__ == "__main__":
    main()
