from random import randint
import re

FIELD_SIZE = 10
MINES_QUANTITY = 10
EMPTY_CELL = '.'
MINE = 'M'
NUMBER_PROMPT = '>> Enter \'X,Y\' coordinates in range (0 - %s): '


def create_field():
    """
    Returns field for game
    """
    return [
        [EMPTY_CELL for _ in range(FIELD_SIZE)]
        for _ in range(FIELD_SIZE)
        ]


def get_random_coord(field_size):
    """
    Returns random coordinate
    """
    return randint(0, field_size - 1)


def set_mines(field):
    """
    Returns random mined field for game
    """
    mines = 0
    while mines < MINES_QUANTITY:
        x, y = get_random_coord(FIELD_SIZE), get_random_coord(FIELD_SIZE)
        if field[x][y] != EMPTY_CELL:
            continue
        field[x][y] = MINE
        mines += 1
    return field


def is_coords_in_range(x, y):
    return 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE


def is_mine(field, x, y):
    return field[x][y] == MINE


def mines_calculation(field):
    """
    Returns the quantity of mines in neighboring cells
    """
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if field[i][j] != MINE:
                mines = 0
                for range_x in (-1, 0, 1):
                    for range_y in (-1, 0, 1):
                        x_offset, y_offset = i + range_x, j + range_y
                        if is_coords_in_range(x_offset, y_offset) and \
                                is_mine(field, x_offset, y_offset):
                            mines += 1
                field[i][j] = mines

            if field[i][j] == 0:
                field[i][j] = '-'

    return field


def action():
    """
    Choose an action to open the cell or mark as Flag
    """
    while True:
        print()
        act = input('> Your input: ').upper()
        if act in ('O', 'M', 'R', 'Q'):
            return act


def input_coordinates():
    """
    Inputs of cell coordinates
    """
    while True:
        try:
            input_str = input(NUMBER_PROMPT % (FIELD_SIZE - 1))
            input_list = re.split(r',', input_str)
            x, y = int(input_list[0]), int(input_list[1])
            if not is_coords_in_range(x, y):
                raise TypeError
            return [y, x]
        except ValueError:
            print('Wrong input. Enter your coordinates in \'X,Y\' format. Try again.')
            print()
        except TypeError:
            print('Your coordinates are out of range. Try again.')
            print()
        except IndexError:
            print('Wrong input. Enter your coordinates in \'X,Y\' format. Try again.')
            print()


def open_cell(field, x, y):
    """
    Checking box on the presence of mines
    """
    if field[x][y] != MINE:
        return True
    else:
        return False


def mark_mine(field, x, y):
    """
    Mark mine on the field
    """
    field[x][y] = MINE
    return field


def remove_mark(field, x, y):
    """
    Remove mine's mark from the field
    """
    if field[x][y] != MINE:
        pass
    else:
        field[x][y] = EMPTY_CELL
    return field


def show_field(field):
    print()
    print('   ', end='')
    for digits in range(FIELD_SIZE):
        print(digits, ' ', end='')
    print()

    for i in range(FIELD_SIZE):
        print(i, ' ', end='')
        for j in range(FIELD_SIZE):
            print(field[i][j], ' ', end='')
        print()


def check_result(field):
    result = 0
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            if top_field[i][j] == bottom_field[i][j]:
                result += 1

    if result == FIELD_SIZE ** 2:
        print('\nCongratulation! You win!')
        return True
    else:
        return False


bottom_field = mines_calculation(set_mines(create_field()))
top_field = create_field()

print('Enter \'O\' to Open cell\n'
      '      \'M\' to mark Mine\n'
      '      \'R\' to Remove mark\n'
      '      \'Q\' to Quit')

show_field(top_field)

while True:
    do_action = action()

    if do_action == 'Q':
        break

    position = input_coordinates()
    x, y = position[0], position[1]

    if do_action == 'O':
        if open_cell(bottom_field, x, y) is True:
            top_field[x][y] = bottom_field[x][y]
        else:
            top_field[x][y] = bottom_field[x][y]
            print('You lose! There is a mine.')
            break
    elif do_action == 'M':
        top_field = mark_mine(top_field, x, y)
    else:
        top_field = remove_mark(top_field, x, y)

    if check_result(show_field(top_field)) == True:
        break