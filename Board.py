from constants import *

class Board:
	'''
	Class containing model for Board of the Game
	'''
	def __init__(self, board_width=MIN_WIDTH, board_height=MIN_HEIGHT):
		if board_width < MIN_WIDTH or board_height < MIN_HEIGHT:
			raise Exception('Either Board width is less than' + MIN_WIDTH + ' or height is less than ' + MIN_HEIGHT)
		self.width = board_width
		self.height = board_height
		self.arena = []

	def __str__(self):
		objString = ''
		for i in range(0, self.height):
			for j in range(0, self.width):
				objString += self.arena[i][j]
			objString += '\n'
		return objString

	def scaledBoard(self):
		objString = ''
		for i in range(0, self.height):
			for y in range(0, Y_SCALE):
				for j in range(0, self.width):
					for x in range(0, X_SCALE):
						objString += self.arena[i][j]
				objString += '\n'
				
		return objString
