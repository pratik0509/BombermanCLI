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

	def explode(self, BombermanBoard):
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
			BombermanBoard.arena[x][y] = EXPSIGN
		if not BombermanBoard.arena[x][y + 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y + 1])
			BombermanBoard.arena[x][y + 1] = EXPSIGN
		if not BombermanBoard.arena[x][y - 1] == WL:
			SCORE += self.__check(BombermanBoard.arena[x][y - 1])
			BombermanBoard.arena[x][y - 1] = EXPSIGN
		if not BombermanBoard.arena[x + 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x + 1][y])
			BombermanBoard.arena[x + 1][y] = EXPSIGN
		if not BombermanBoard.arena[x - 1][y] == WL:
			SCORE += self.__check(BombermanBoard.arena[x - 1][y])
			BombermanBoard.arena[x - 1][y] = EXPSIGN
		return str(True), SCORE

	def removeExplosion(self, BombermanBoard):
		x = self.x_pos
		y = self.y_pos
		SCORE = 0
		if self.endTime > getTimeMillis():
			return
		if BombermanBoard.arena[x][y] == EXPSIGN:
			BombermanBoard.arena[x][y] = ' '
		if BombermanBoard.arena[x][y + 1] == EXPSIGN:
			BombermanBoard.arena[x][y + 1] = ' '
		if BombermanBoard.arena[x][y - 1] == EXPSIGN:
			BombermanBoard.arena[x][y - 1] = ' '
		if BombermanBoard.arena[x + 1][y] == EXPSIGN:
			BombermanBoard.arena[x + 1][y] = ' '
		if BombermanBoard.arena[x - 1][y] == EXPSIGN:
			BombermanBoard.arena[x - 1][y] = ' '
		return True
