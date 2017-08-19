from random import randint
from constants import *
from math import ceil
from time import time

def getTimeMillis():
	return int(round(time() * 1000))

class Bomb:
	'''
	Bomb class
	'''

	def __init__(self, x_pos, y_pos):
		self.plantTime = getTimeMillis()
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.endTime = getTimeMillis() + PTIME

	def remainingTime(self):
		return ceil((ETIME - (getTimeMillis() - self.plantTime)) / 1000)

	def __check(self, code):
		if code == BR:
			return BREAK_BRICK
		elif code == EM:
			return BREAK_ENEMY
		return 0

	def explode(self, BombermanBoard, EnemyList):
		if BombermanBoard.arena[self.x_pos][self.y_pos] == ' ' or \
		BombermanBoard.arena[self.x_pos][self.y_pos] == '2' or \
		BombermanBoard.arena[self.x_pos][self.y_pos] == '1' or \
		BombermanBoard.arena[self.x_pos][self.y_pos] == '0' or \
		BombermanBoard.arena[self.x_pos][self.y_pos] == '-1':
			BombermanBoard.arena[self.x_pos][self.y_pos] = str(self.remainingTime())
		if self.remainingTime() > 0:
			return str(False), 0
		x = self.x_pos
		y = self.y_pos
		SCORE = 0
		if not BombermanBoard.arena[x][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y])
			rmEnemy(EnemyList, x, y, BombermanBoard)
			BombermanBoard.arena[x][y] = EXPSIGN
		if not BombermanBoard.arena[x][y + 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y + 1])
			rmEnemy(EnemyList, x, y + 1, BombermanBoard)
			BombermanBoard.arena[x][y + 1] = EXPSIGN
		if not BombermanBoard.arena[x][y - 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y - 1])
			rmEnemy(EnemyList, x, y - 1, BombermanBoard)
			BombermanBoard.arena[x][y - 1] = EXPSIGN
		if not BombermanBoard.arena[x + 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x + 1][y])
			rmEnemy(EnemyList, x + 1, y, BombermanBoard)
			BombermanBoard.arena[x + 1][y] = EXPSIGN
		if not BombermanBoard.arena[x - 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x - 1][y])
			rmEnemy(EnemyList, x - 1, y, BombermanBoard)
			BombermanBoard.arena[x - 1][y] = EXPSIGN
		return str(True), SCORE

	def removeExplosion(self, BombermanBoard, EnemyList):
		x = self.x_pos
		y = self.y_pos
		SCORE = 0
		if not BombermanBoard.arena[x][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y])
			rmEnemy(EnemyList, x, y, BombermanBoard)
			BombermanBoard.arena[x][y] = EXPSIGN
		if not BombermanBoard.arena[x][y + 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y + 1])
			rmEnemy(EnemyList, x, y + 1, BombermanBoard)
			BombermanBoard.arena[x][y + 1] = EXPSIGN
		if not BombermanBoard.arena[x][y - 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y - 1])
			rmEnemy(EnemyList, x, y - 1, BombermanBoard)
			BombermanBoard.arena[x][y - 1] = EXPSIGN
		if not BombermanBoard.arena[x + 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x + 1][y])
			rmEnemy(EnemyList, x + 1, y, BombermanBoard)
			BombermanBoard.arena[x + 1][y] = EXPSIGN
		if not BombermanBoard.arena[x - 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x - 1][y])
			rmEnemy(EnemyList, x - 1, y, BombermanBoard)
			BombermanBoard.arena[x - 1][y] = EXPSIGN

		if self.endTime > getTimeMillis():
			return
		if BombermanBoard.arena[x][y] == EXPSIGN:
			BombermanBoard.arena[x][y] = ' '
			rmEnemy(EnemyList, x, y, BombermanBoard)
		if BombermanBoard.arena[x][y + 1] == EXPSIGN:
			BombermanBoard.arena[x][y + 1] = ' '
			rmEnemy(EnemyList, x, y + 1, BombermanBoard)
		if BombermanBoard.arena[x][y - 1] == EXPSIGN:
			BombermanBoard.arena[x][y - 1] = ' '
			rmEnemy(EnemyList, x, y - 1, BombermanBoard)
		if BombermanBoard.arena[x + 1][y] == EXPSIGN:
			BombermanBoard.arena[x + 1][y] = ' '
			rmEnemy(EnemyList, x + 1, y, BombermanBoard)
		if BombermanBoard.arena[x - 1][y] == EXPSIGN:
			BombermanBoard.arena[x - 1][y] = ' '
			rmEnemy(EnemyList, x - 1, y, BombermanBoard)
		return True

def rmEnemy(EnemyList, x, y, BombermanBoard):
	for e in EnemyList:
		if e.x_pos == x and e.y_pos == y:
			BombermanBoard.arena[e.x_pos][e.y_pos] = ' '
			EnemyList.remove(e)
