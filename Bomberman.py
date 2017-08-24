from Person import Person
from constants import BM


class Bomberman(Person):
    '''
    Class for Bomberman
    '''

    def __init__(self):
        self.x_pos = 1
        self.y_pos = 1

    def alive(self, BombermanBoard):
        return BombermanBoard.arena[self.x_pos][self.y_pos] == BM
