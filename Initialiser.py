from random import randint
from Board import Board
from constants import *
from Brick import Brick
import os
from Bomberman import Bomberman
from Enemy import Enem


EnemyList = []
Player = ''
BombermanBoard = ''

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


def loadBoard():
	BombermanBoard = Board()
	placeWalls(BombermanBoard)
	placeBricks(BombermanBoard)
	placeEnemies(BombermanBoard)
	Player = placeBomberMan(BombermanBoard)
	for i in range(0, 100):
		os.system('clear')
		for e in EnemyList:
			e.move(RMV[randint(0, 3)], BombermanBoard, EM)
		Player.move(RMV[randint(0, 3)], BombermanBoard, BM)
		print(BombermanBoard.scaledBoard())
		os.system('sleep 0.13')
loadBoard()
