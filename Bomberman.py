from Person import Person
from constants import BM

class Bomberman(Person):
	'''
	Class for Bomberman
	'''

	def __init__(self, board_height, board_width):
		super().__init__(board_height, board_width)

	def alive(self, BombermanBoard):
		return BombermanBoard.arena[self.x_pos][self.y_pos] == BM
