import time
from random import seed, randint

seed(time.time())

class Bomb:
	'''
	Bomb class
	'''

	def __init__(self, x_pos, y_pos):
		self.plantTime = getMillis()
		self.destructTime = self.plantTime + 900 + randint(0, 50)
		self.x_pos = x_pos
		self.y_pos = y_pos

	def getMillis():
		return int(round(time.time() * 1000))
