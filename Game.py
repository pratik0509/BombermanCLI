from constants import *				# Game Play/State constants
from random import randint			# For generating random numbers
from Board import Board
from Brick import Brick
from os import system
import time
from Bomberman import Bomberman
from Enemy import Enemy
from Input import NonBlockInput
from sys import exit
from Bomb import Bomb

Inp = NonBlockInput()
EnemyList = []
BombList = []
ExplosionList = []
level = LEVEL[1]


class Gate:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y


def gameEnded(SCORE): 					# Called when Game ends to print the final score
    print(color.HRED + 'GAME OVER...!!!' + '\t' + color.HGREEN +
          ' SCORE:' + str(SCORE) + color.END)
    system('sleep 2')
    exit(0)


def getTimeMillis():					# Get time in milliseconds
    return int(round(time.time() * 1000))


def placeWalls(BombermanBoard):			# Place the walls on the board
    for i in range(0, BombermanBoard.height):
        BombermanBoard.arena.append([])
        for j in range(0, BombermanBoard.width):
            BombermanBoard.arena[i].append(' ')

    for i in range(0, BombermanBoard.height):
        BombermanBoard.arena[i][BombermanBoard.width - 1] = WL
        BombermanBoard.arena[i][0] = WL

    for i in range(0, BombermanBoard.width):
        BombermanBoard.arena[BombermanBoard.height - 1][i] = WL
        BombermanBoard.arena[0][i] = WL

    for i in range(2, BombermanBoard.height):
        for j in range(2, BombermanBoard.width):
            if i % 2 == 0 and j % 2 == 0:
                BombermanBoard.arena[i][j] = WL


def placeBricks(BombermanBoard):					# Place the bricks on the board
    for i in range(0, MAX_BRICKS):
        block = Brick(BombermanBoard.height, BombermanBoard.width)
        while not BombermanBoard.placeObject(block.x_pos, block.y_pos, BR):
            block = Brick(BombermanBoard.height, BombermanBoard.width)
    # Return the brick inside which gate is located
    return Gate(block.x_pos, block.y_pos)


def placeBomberMan(BombermanBoard):					# Place Bomberman on the board
    man = Bomberman()
    BombermanBoard.placeObject(man.x_pos, man.y_pos, BM)
    return man


def placeEnemies(BombermanBoard):					# Place enemies on the board
    for i in range(0, MAX_ENEMY):
        block = Enemy(BombermanBoard.height, BombermanBoard.width)
        while not BombermanBoard.placeObject(block.x_pos, block.y_pos, EM):
            block = Enemy(BombermanBoard.height, BombermanBoard.width)
            # Append the enemies to the alive enemy list
        EnemyList.append(block)


# Move the pieces on the board
def moveHandler(keyPress, Player, BombermanBoard, SCORE):
    if keyPress == QUIT:
        exit(0)
    elif keyPress == PAUSE:
        input('Press <ENTER> to continue...')
    elif keyPress == EDROP and len(BombList) < MAX_BOMB_ALLOWED:
        BombList.append(Bomb(Player.x_pos, Player.y_pos))
    elif keyPress in MV:
        if not Player.move(keyPress, BombermanBoard, BM):
            return True
    return False


def loadBoard():			# The main function where all starts ;)
    SCORE = 0
    lifes = 3				# Life awarded to the user
    for i in range(1, 8):
        flag = False
        while lifes > 0 and not flag:
            system('sleep 0.5')		# Pause before the game starts

            level = LEVEL[i]
            del EnemyList[:]		# Clear the Lists
            del BombList[:]
            del ExplosionList[:]

            if level < LEVEL[5]:		# Check for xtreme levels
                MAX_ENEMY = MAX_ENEMYX
                MAX_BRICKS = MAX_BRICKSX

            BombermanBoard = Board()		# Initialize the board
            placeWalls(BombermanBoard)
            Player = placeBomberMan(BombermanBoard)
            NewGate = placeBricks(BombermanBoard)
            placeEnemies(BombermanBoard)
            WATCH = 200					# Timeout for the game
            STYM = getTimeMillis()
            flag = False				# Level not finished yet
            while True and not flag:
                # Clear the screen for displaying the board properly
                system('clear')
                if BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] != BR and\
                   BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] != BM:
                    BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] = GT
                # Check if the player is still alive
                if not Player.alive(BombermanBoard):
                    lifes -= 1
                    break

                if Inp.kbhit():		# Check for input
                    lifeCheck = True
                    if moveHandler(Inp.getch(), Player, BombermanBoard, SCORE):
                        lifeCheck = False
                        # Flush the input buffer so that remaining characters
                        # are discarded
                        Inp.flush()
                    if not lifeCheck:
                        lifes -= 1
                        break

                tym = getTimeMillis()
                for e in EnemyList:		# Loop over the enemies to move them
                    if e.endTime + e.pauseTime + level < tym:
                        e.move(RMV[randint(0, 3)], BombermanBoard, EM, tym)
                # loop over the dormant bombs to find out the exploding ones
                for b in BombList:
                    check, sc = b.explode(BombermanBoard, EnemyList)
                    if check == 'True':
                        SCORE += sc
                        ExplosionList.append(b)
                        BombList.remove(b)

                for e in ExplosionList:				# Loop over the exploding bombs
                    if e.removeExplosion(BombermanBoard, EnemyList):
                        ExplosionList.remove(e)

                if getTimeMillis() > STYM + 1000:
                    STYM = getTimeMillis()
                    WATCH -= 1

                if WATCH < 1:
                    lifes -= 1
                    break

                if len(EnemyList) == 0 and\
                   Player.x_pos == NewGate.x_pos and\
                   Player.y_pos == NewGate.y_pos:
                    SCORE += int(TIME_BONUS * WATCH) + LEVEL_BONUS // level
                    flag = True
                # Print the score and lifes with board
                print(BombermanBoard.scaledBoard(SCORE, WATCH) + 'LEVEL: ' +
                      str(i) + '\tLIFE: ' + str(lifes))
                system('sleep 0.08')		# For proper display of frames
    gameEnded(SCORE)  # When game ends display the scores

if __name__ == '__main__':
    loadBoard()
