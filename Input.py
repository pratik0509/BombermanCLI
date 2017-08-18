import sys
from select import select
import atexit
import termios

class NonBlockInput:

	def __init__(self):

		# Save the terminal settings
		self.fileDescriptor = sys.stdin.fileno()
		self.newTerm = termios.tcgetattr(self.fileDescriptor)
		self.oldTerm = termios.tcgetattr(self.fileDescriptor)

		# New terminal setting unbuffered
		self.newTerm[3] = (self.newTerm[3] & ~termios.ICANON & ~termios.ECHO)
		termios.tcsetattr(self.fileDescriptor, termios.TCSAFLUSH, self.newTerm)


	def kbhit(self):
		dr, dw, de = select([sys.stdin], [], [], 0)
		return dr != []

	def getch(self):
		return sys.stdin.read(1)
