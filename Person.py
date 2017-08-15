class Person:
	'''
	Person class
	'''

	def __init__(self, x_coord, y_coord):
		self.x_pos = x_coord
		self.y_pos = y_coord

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
