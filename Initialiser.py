from Board import Board
from constants import *
from Brick import Brick
import os

def placeWalls(BombermanBoard):
	for i in range(0, BombermanBoard.height):
		BombermanBoard.arena.append([])
		for j in range(0, BombermanBoard.width):
			BombermanBoard.arena[i].append(' ')

	for i in range(0, BombermanBoard.height):
		BombermanBoard.arena[i][BombermanBoard.width - 1] = '#'
		BombermanBoard.arena[i][0] = '#'

		for i in range(0, BombermanBoard.width):
			BombermanBoard.arena[BombermanBoard.height - 1][i] = '#'
			BombermanBoard.arena[0][i] = '#'

	for i in range(2, BombermanBoard.height):
		for j in range(2, BombermanBoard.width):
			if i % 2 == 0 and j % 2 == 0:
				BombermanBoard.arena[i][j] = '#'
	pass

def placeBricks(BombermanBoard):
	for i in range(0, MAX_BRICKS):
		block = Brick(BombermanBoard.height ,BombermanBoard.width)
		while not BombermanBoard.placeObject(block.x_pos, block.y_pos, '%') :
			block = Brick(BombermanBoard.height ,BombermanBoard.width)

def loadBoard():
	os.system('clear')
	BombermanBoard = Board()
	placeWalls(BombermanBoard)
	placeBricks(BombermanBoard)
	print(BombermanBoard.scaledBoard())

loadBoard()
