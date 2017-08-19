from constants import *
from random import randint
from Board import Board
from Brick import Brick
import os
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

def getTimeMillis():
	return int(round(time.time() * 1000))

def placeWalls(BombermanBoard):
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

def placeBricks(BombermanBoard):
	for i in range(0, MAX_BRICKS):
		block = Brick(BombermanBoard.height ,BombermanBoard.width)
		while not BombermanBoard.placeObject(block.x_pos, block.y_pos, BR) :
			block = Brick(BombermanBoard.height ,BombermanBoard.width)
	return Gate(block.x_pos, block.y_pos)

def placeBomberMan(BombermanBoard):
	man = Bomberman()
	BombermanBoard.placeObject(man.x_pos, man.y_pos, BM)
	return man

def placeEnemies(BombermanBoard):
	for i in range(0, MAX_ENEMY):
		block = Enemy(BombermanBoard.height ,BombermanBoard.width)
		while not BombermanBoard.placeObject(block.x_pos, block.y_pos, EM) :
			block = Enemy(BombermanBoard.height ,BombermanBoard.width)
		EnemyList.append(block)

def moveHandler(keyPress, Player, BombermanBoard, SCORE):
	if keyPress == QUIT:
		exit(0)
	elif keyPress == PAUSE:
		input('Press <ENTER> to continue...')
	elif keyPress == EDROP and len(BombList) < MAX_BOMB_ALLOWED:
		BombList.append(Bomb(Player.x_pos, Player.y_pos))
	elif keyPress in MV:
		if not Player.move(keyPress, BombermanBoard, BM):
			print(color.HRED + 'GAME OVER...!!!' + '\t' + color.HGREEN + ' SCORE:' + str(SCORE) + color.END)
			os.system('sleep 2')
			exit(0)
	return

def loadBoard():
	SCORE = 0
	for i in  range(1, 11):
		os.system('sleep 0.5')
		level = LEVEL[i]
		if level < LEVEL[5]:
			MAX_ENEMY = MAX_ENEMYX
			MAX_BRICKS = MAX_BRICKSX
		BombermanBoard = Board()
		placeWalls(BombermanBoard)
		Player = placeBomberMan(BombermanBoard)
		NewGate = placeBricks(BombermanBoard)
		placeEnemies(BombermanBoard)
		STYM = getTimeMillis()
		WATCH = 200
		flag = False
		while True and not flag:
			os.system('clear')
			if BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] != BR and\
			 BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] != BM:
				BombermanBoard.arena[NewGate.x_pos][NewGate.y_pos] = GT
			if not Player.alive(BombermanBoard):
				print(color.HRED + 'GAME OVER...!!!' + '\t' + color.HGREEN + ' SCORE:' + str(SCORE) + color.END)
				os.system('sleep 2')
				exit(0)

			if Inp.kbhit():
				moveHandler(Inp.getch(), Player, BombermanBoard, SCORE)
				Inp.flush()

			tym = getTimeMillis()
			for e in EnemyList:
				if e.endTime + level < tym:
					e.move(RMV[randint(0, 3)], BombermanBoard, EM, tym)

			for b in BombList:
				check, sc = b.explode(BombermanBoard, EnemyList)
				if check == 'True':
					SCORE += sc
					ExplosionList.append(b)
					BombList.remove(b)

			for e in ExplosionList:
				if e.removeExplosion(BombermanBoard, EnemyList):
					ExplosionList.remove(e)
			if getTimeMillis() > STYM + 1000:
				STYM = getTimeMillis()
				WATCH -= 1
			if WATCH < 1:
				print(color.HRED + 'GAME OVER...!!!' + '\t' + color.HGREEN + ' SCORE:' + str(SCORE) + color.END)
				os.system('sleep 2')
				exit(0)
			if len(EnemyList) == 0 and [Player.x_pos, Player.y_pos] == [NewGate.x_pos, NewGate.y_pos]:
				SCORE += int(TIME_BONUS * WATCH) + LEVEL_BONUS // level
				flag = True
			print(BombermanBoard.scaledBoard(SCORE, WATCH) + 'LEVEL: ' + str(i))
			os.system('sleep 0.08')

loadBoard()
