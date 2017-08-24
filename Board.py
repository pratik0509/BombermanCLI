from constants import *


class Board:
    '''
    Class containing model for Board of the Game
    '''
    def __init__(self, board_width=MIN_WIDTH, board_height=MIN_HEIGHT):
        if board_width < MIN_WIDTH or board_height < MIN_HEIGHT:
            raise Exception('Either Board width is less than' +
                            MIN_WIDTH + ' or height is less than ' + MIN_HEIGHT)
        self.width = board_width
        self.height = board_height
        self.arena = []

    def __str__(self):
        objString = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                objString += self.arena[i][j]
        objString += '\n'
        return objString

    def scaledBoard(self, SCORE, WATCH):
        objString = ''
        for i in range(0, self.height):
            for y in range(0, Y_SCALE):
                for j in range(0, self.width):
                    for x in range(0, X_SCALE):
                        if self.arena[i][j] == BM:
                            objString += BMAN[y][x]
                        elif self.arena[i][j] == EM:
                            objString += ENEM[y][x]
                        else:
                            objString += self.arena[i][j]
                objString += '\n'

        objString += '\n\n'
        objString += 'SCORE: ' + str(SCORE) + '\t'
        objString += 'TIME: ' + str(WATCH) + '\n'
        return objString

    def placeObject(self, x_pos, y_pos, piece):
        if x_pos == 2 and y_pos == 1:
            return False

        if y_pos == 2 and x_pos == 1:
            return False

        if self.arena[x_pos][y_pos] != ' ':
            return False
        else:
            self.arena[x_pos][y_pos] = piece
        return True
