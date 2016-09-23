from random import randint

FIELD_SIZE = 10
MINES_QUANTITY = 10
EMPTY_CELL = 0
MINE = 'M'
OPENED_CELL = 1
MINE_SIGN = 'F'

NUMBER_PROMPT = 'Write number of line from 0 to %s:'


def create_field():
    """
    returns field for minesweeper game
    """
    return [
        [EMPTY_CELL for _ in range(FIELD_SIZE)]
        for _ in range(FIELD_SIZE)
    ]


def get_random_coord(field_size):
    return randint(0, field_size - 1)


def set_mines(field):
    """
    returns random mined field for game
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


def is_mine(x, y):
    return field[x][y] == MINE


def mine_calculation(field, x, y):
    """
    returns the quantity of mines in neighboring cells
    """
    if field[x][y] == MINE:
        return 'M'

    mines = 0
    for range_x in (-1, 0, 1):
        for range_y in (-1, 0, 1):
            x_offset, y_offset = x + range_x, y + range_y
            if is_coords_in_range(x_offset, y_offset) and \
                    is_mine(x_offset, y_offset):
                mines += 1
    return mines


def input_coordinates():
    """
    Inputs of cell coordinates
    """
    while True:
        try:
            x = int(input(NUMBER_PROMPT % (FIELD_SIZE-1)))
            y = int(input(NUMBER_PROMPT % (FIELD_SIZE-1)))
            if not is_coords_in_range(x, y):
                raise TypeError
            return x, y
        except ValueError:
            print('Wrong input, try again')
        except TypeError:
            print('Your number of coordinate is out of field')


def validate_action_coords(field, x, y):
    """
    Check for repeated call to the cell
    """
    return field[x][y] == EMPTY_CELL


def action():
    """
    Choose an action to open the cell or mark as Flag
    """
    while True:
        act = input('Enter O - to open cell / F - to mark as FLAG:  ').upper()
        if act in ('O', 'F'):
            return act

do_action = action()


bottom_field = create_field()
top_field = create_field()
field = set_mines(bottom_field)

# show playground with mines
for row in field:
    for cell in row:
        print(cell, end=' ')
    print()

print()

# show mines q-ty
for i in range(len(field)):
    for j in range(len(field[i])):
        print(mine_calculation(field, i, j), end=' ')
    print()

def mark_mine(x, y, flag, playing_field):
    """
    marking filed
    x, y -- from 'def input_coordinates():'
    flag -- from 'def action(coords):'
    playing_field -- from 'def creating_playing_field():'
    """
    if flag == 'F':
        playing_field[x][y] = 'F'
        

def open_cell (x,y, field):
    """ 
    checking box on the presence of mines
    """
    if field[x][y] == EMPTY_CELL:
        print ('Empty cell')
        field[x][y] = mine_calculation(field, x, y)
    if field[x][y] == MINE:
        print ('You lost')
