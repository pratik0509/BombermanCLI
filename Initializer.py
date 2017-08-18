from random import randint
from Board import Board
from constants import *
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
# Player = ''
# BombermanBoard = ''
level = LEVELZ

if level < LEVEL4:
	MAX_ENEMY = MAX_ENEMYX
	MAX_BRICKS = MAX_BRICKSX

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

def placeBomberMan(BombermanBoard):
	man = Bomberman(BombermanBoard.height, BombermanBoard.width)
	while not BombermanBoard.placeObject(man.x_pos, man.y_pos, BM):
		man = Bomberman(BombermanBoard.height, BombermanBoard.width)
	return man

def placeEnemies(BombermanBoard):
	for i in range(0, MAX_ENEMY):
		block = Enemy(BombermanBoard.height ,BombermanBoard.width)
		while not BombermanBoard.placeObject(block.x_pos, block.y_pos, EM) :
			block = Enemy(BombermanBoard.height ,BombermanBoard.width)
		EnemyList.append(block)

def moveHandler(keyPress, Player, BombermanBoard):
	if keyPress == QUIT:
		exit(0)
	elif keyPress == PAUSE:
		input('Press <ENTER> to continue...')
	elif keyPress == EDROP:
		BombList.append(Bomb())
	elif keyPress in MV:
		Player.move(keyPress, BombermanBoard, BM)
	return

def loadBoard():
	BombermanBoard = Board()
	placeWalls(BombermanBoard)
	placeBricks(BombermanBoard)
	placeEnemies(BombermanBoard)
	Player = placeBomberMan(BombermanBoard)
	while True:
		os.system('clear')
		if Inp.kbhit():
			moveHandler(Inp.getch(), Player, BombermanBoard)
			# Player.move(Inp.getch(), BombermanBoard, BM)
		tym = getTimeMillis()
		for e in EnemyList:
			if e.endTime + level < tym:
				e.move(RMV[randint(0, 3)], BombermanBoard, EM, tym)
		for b in BombList:
			if b.remainingTime() <= 0:
				b.explode(BombermanBoard)
		print(BombermanBoard.scaledBoard())
		os.system('sleep 0.08')
loadBoard()
