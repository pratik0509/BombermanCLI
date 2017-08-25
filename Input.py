import sys
from select import select
import termios


class NonBlockInput:
    # Constructor
    def __init__(self):
        self.fileDescriptor = sys.stdin.fileno()
        self.newTerm = termios.tcgetattr(self.fileDescriptor)
        self.oldTerm = termios.tcgetattr(self.fileDescriptor)

        self.newTerm[3] &= (~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fileDescriptor, termios.TCSAFLUSH, self.newTerm)

    # Check the availability of character in STDIN
    def kbhit(self):
        dr, dw, de = select([sys.stdin], [], [], 0)
        return dr != []

    # Get one character from STDIN
    def getch(self):
        return sys.stdin.read(1)

    # Flush the input stream
    def flush(self):
        termios.tcflush(self.fileDescriptor, termios.TCIFLUSH)

    # Destructor to restore the previous terminal state
    def __del__(self):
        termios.tcsetattr(self.fileDescriptor, termios.TCSANOW, self.oldTerm)
