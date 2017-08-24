from random import randint


class Brick:
    '''
    Brick class for defining bricks
    '''

    def __init__(self, board_height, board_width):
        self.x_pos = randint(1, board_width - 1)
        self.y_pos = randint(1, board_height - 1)
