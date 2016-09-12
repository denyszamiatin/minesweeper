from random import randint
FIELD_SIZE = 10
EMPTY_CELL = 0
MINE_INDICATOR = 'M'


def get_playing_field():
    """
    returns field for minesweeper game
    """
    return [
        [EMPTY_CELL for i in range(FIELD_SIZE)]
        for i in range(FIELD_SIZE)
    ]


def get_mined_field():
    """
    returns random mined field for game
    """
    mined_field = []
    for i, j in enumerate(get_playing_field()):
        j.insert(randint(0, FIELD_SIZE), MINE_INDICATOR)
        mined_field.append(j)
    return mined_field


def mine_calculation(array, x, y):
    """
    returns the quantity of mines in neighboring cells
    """
    mine_qty = 0

    if array[x][y] == MINE_INDICATOR:
        return 'M'
    else:
        for range_x in (-1, 0, 1):
            for range_y in (-1, 0, 1):
                if x + range_x >= 0 and y + range_y >= 0:
                    try:
                        cell_check = array[x + range_x][y + range_y]
                    except IndexError:
                        break
                    else:
                        if cell_check == MINE_INDICATOR:
                            mine_qty += 1
        return mine_qty


playground = (get_mined_field())

#show playground with mines
for i in range(len(playground)):
    for j in range(len(playground[i])):
        print(playground[i][j], end=' ')
    print()

print()

#show mines q-ty
for i in range(len(playground)):
    for j in range(len(playground[i])):
        print(mine_calculation(playground, i, j), end=' ')
    print()