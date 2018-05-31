from random import randint
from constants import MV, BM, EM, EXPSIGN, BR, WL


class Person:
    '''
    Person class
    '''

    def __init__(self, board_height, board_width):
        self.x_pos = randint(1, board_width - 1)
        self.y_pos = randint(1, board_height - 1)

    def moveValidity(self, Arena):
        validMove = [True, True, True, True]
        mvpos = 0

        x = self.x_pos
        y = self.y_pos

        validMove[0] &= not (Arena[x][y + 1] == BR or Arena[x][y + 1] == WL)
        validMove[1] &= not (Arena[x + 1][y] == BR or Arena[x + 1][y] == WL)
        validMove[2] &= not (Arena[x][y - 1] == BR or Arena[x][y - 1] == WL)
        validMove[3] &= not (Arena[x - 1][y] == BR or Arena[x - 1][y] == WL)

        return validMove

    def move(self, keyPress, BombermanBoard, code):
        x = self.x_pos
        y = self.y_pos

        availMoves = self.moveValidity(BombermanBoard.arena)

        if not availMoves[MV[keyPress]]:
            return True

        BombermanBoard.arena[x][y] = ' '

        if MV[keyPress] == 0:
            y += 1
        elif MV[keyPress] == 1:
            x += 1
        elif MV[keyPress] == 2:
            y -= 1
        elif MV[keyPress] == 3:
            x -= 1

        if code == BM:
            if BombermanBoard.arena[x][y] == EM or\
             BombermanBoard.arena[x][y] == EXPSIGN:
                return False

        BombermanBoard.arena[x][y] = code
        self.x_pos = x
        self.y_pos = y
        return True
