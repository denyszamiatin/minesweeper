FIELD_SIZE = 10
EMPTY_CELL = 0


def get_playing_field():
    """

    :return:
    """
    return [
        [EMPTY_CELL for i in range(FIELD_SIZE)]
        for i in range(FIELD_SIZE)
    ]

print(get_playing_field())
