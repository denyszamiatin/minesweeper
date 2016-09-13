from random import randint

FIELD_SIZE = 10
MINES_QUANTITY = 10
EMPTY_CELL = 0
MINE = 'M'


def get_playing_field():
    """
    returns field for minesweeper game
    """
    return [
        [EMPTY_CELL for i in range(FIELD_SIZE)]
        for i in range(FIELD_SIZE)
    ]


def get_random_coord(field_size):
    return randint(0, field_size - 1)


def set_mines(field):
    """
    returns random mined field for game
    """
    mines = 0
    while mines < MINES_QUANTITY:
        x = get_random_coord(FIELD_SIZE)
        y = get_random_coord(FIELD_SIZE)
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
            x_offset = x + range_x
            y_offset = y + range_y
            if is_coords_in_range(x_offset, y_offset) and \
                    is_mine(x_offset, y_offset):
                mines += 1
    return mines


field = set_mines(get_playing_field())


#show playground with mines
for row in field:
    for cell in row:
        print(cell, end=' ')
    print()

print()

#show mines q-ty
for i in range(len(field)):
    for j in range(len(field[i])):
        print(mine_calculation(field, i, j), end=' ')
    print()
    
    
def input_coordinates():
    """
    Inputs of cell coordinates
    """
    while True:
        try:
            x = int(input('Write number of line from 0 to %s:' %(FIELD_SIZE-1)))
            y = int(input('Write number of line from 0 to %s:' %(FIELD_SIZE-1)))
            if not is_coords_in_range(x, y):
                raise TypeError
            return x, y
        except ValueError:
            print('Wrong input, try again')
        except TypeError:
            print('Your number of coordinate is out of field')

print(input_coordinates())
