from random import randint
from constants import *
from math import ceil

class Bomb:
	'''
	Bomb class
	'''

	def __init__(self, x_pos, y_pos):
		self.plantTime = getMillis()
		self.x_pos = x_pos
		self.y_pos = y_pos

	def remainingTime(self):
		return ceil((ETIME - (getTimeMillis() - self.plantTime)) / 1000)

	def getMillis():
		return int(round(time.time() * 1000))

	def explode(self, BombermanBoard):
		if self.remainingTime() > 0:
			return
		x = self.x_pos
		y = self.y_pos

		if not BombermanBoard.arena[x][y] == WL:
				BombermanBoard.arena[x][y] = EXPSIGN
		if not BombermanBoard.arena[x][y + 1] == WL:
				BombermanBoard.arena[x][y + 1] = EXPSIGN
		if not BombermanBoard.arena[x][y - 1] == WL:
				BombermanBoard.arena[x][y - 1] = EXPSIGN
		if not BombermanBoard.arena[x + 1][y] == WL:
				BombermanBoard.arena[x + 1][y] = EXPSIGN
		if not BombermanBoard.arena[x - 1][y] == WL:
			BombermanBoard.arena[x - 1][y] = EXPSIGN
