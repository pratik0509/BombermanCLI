from Person import Person
import time


class Enemy(Person):
	'''
	Class for Enemy
	'''

	def __init__(self, board_height, board_width):
		super().__init__(board_height, board_width)
		self.endTime = int(round(time.time() * 1000))
		self.pauseTime = (7 * int(round(time.time() * 1000))) % 149

	def move(self, keyPress, BombermanBoard, code, tym):
		chk = super().move(keyPress, BombermanBoard, code)
		self.endTime = tym
		return chk
