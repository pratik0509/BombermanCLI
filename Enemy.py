from Person import Person

class Enemy(Person):
	'''
	Class for Enemy
	'''

	def __init__(self, board_height, board_width):
		super().__init__(board_height, board_width)
