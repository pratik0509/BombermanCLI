from constants import *

class Board:
	'''
	Class containing model for Board of the Game
	'''
	def __init__(self, board_width, board_height):
		if board_width < MIN_WIDTH or board_height < MIN_HEIGHT:
			raise Exception('Either Board width is less than' + MIN_WIDTH + ' or height is less than ' + MIN_HEIGHT)
		self.width = board_width | MIN_WIDTH
		self.height = board_height | MIN_WIDTH
		self.board[self.width][self.height]
