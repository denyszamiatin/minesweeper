from random import randint
FIELD_SIZE = 10
EMPTY_CELL = 0


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
        j.insert(randint(0, FIELD_SIZE), 'M')
        mined_field.append(j)
    return mined_field

print(get_mined_field())


