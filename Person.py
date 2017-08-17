import time
from random import seed, randint

seed(time.time())

class Person:
	'''
	Person class
	'''

	def __init__(self, board_height, board_width):
		self.x_pos = randint(1, board_width - 1)
		self.y_pos = randint(1, board_height - 1)

	'''
	TODO: Return in which direction move is valid
	'''
	
	def moveValidity(self, Obstacles):
		validMove = [True, True, True, True]
		mvpos = 0
		for itr in Obstacles:
			validMove[mvpos % 4] &= (itr.x_pos != self.x_pos and itr.y_pos != self.y_pos)
			mvpos += 1

		return validMove
