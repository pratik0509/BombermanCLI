from Person import Person
import time


class Enemy(Person):
    '''
    Class for Enemy
    '''
    # Constructor
    def __init__(self, board_height, board_width):
        super().__init__(board_height, board_width)
        # Store the last time enemy moved in ms
        self.endTime = int(round(time.time() * 1000))
        # Store the random pause time after previous move
        self.pauseTime = (7 * int(round(time.time() * 1000))) % 79

    def move(self, keyPress, BombermanBoard, code, tym):
        chk = super().move(keyPress, BombermanBoard, code)
        self.endTime = tym
        return chk
