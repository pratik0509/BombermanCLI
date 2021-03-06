MIN_WIDTH = 17
MIN_HEIGHT = 17
X_SCALE = 4
Y_SCALE = 2
MAX_BRICKS = 15
MAX_BRICKSX = 20
BMAN = [['[', '^', '^', ']'], [' ', ']', '[', ' ']]
MAX_ENEMY = 5
MAX_ENEMYX = 10
ENEM = [['(', '@', '@', ')'], [' ', ')', '(', ' ']]
MV = {'d': 0, 's': 1, 'a': 2, 'w': 3}
RMV = {0: 'd', 1: 's', 2: 'a', 3: 'w'}
ETIME = 2010
PTIME = ETIME + 500
LEVEL = {
    1: 650,
    2: 500,
    3: 400,
    4: 300,
    5: 200,
    6: 100,
    7: 80,
    }


class CLR:
    GRAY = '\033[1;30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    CRIMSON = '\033[1;38m'
    HRED = '\033[1;41m'
    HGREEN = '\033[1;42m'
    HBROWN = '\033[1;43m'
    HBLUE = '\033[1;44m'
    HMAGENTA = '\033[1;45m'
    HCYAN = '\033[1;46m'
    HGRAY = '\033[1;47m'
    HCRIMSON = '\033[1;48m'
    SBROWN = '\x1b[38;5;215m'
    LRED = '\x1b[38;5;9m'
    LGREEN = '\x1b[38;5;34m'
    LMAGENTA = '\x1b[38;5;13m'
    LYELLOW = '\x1b[38;5;11m'
    END = '\033[1;m'

color = CLR()
BM = '@'
EM = '!'
GT = color.HCYAN + '$' + color.END
BR = color.SBROWN + '%' + color.END
WL = color.LRED + '#' + color.END
EXPSIGN = color.LYELLOW + '^' + color.END
EDROP = 'b'
BSIGN = color.YELLOW + '*' + color.END
for i in range(0, len(BMAN)):
    for j in range(0, len(BMAN[i])):
        BMAN[i][j] = color.LGREEN + BMAN[i][j] + color.END


for i in range(0, len(BMAN)):
    for j in range(0, len(BMAN[i])):
        ENEM[i][j] = color.LMAGENTA + ENEM[i][j] + color.END

QUIT = 'q'
PAUSE = 'p'
BREAK_BRICK = 20
BREAK_ENEMY = 100
LEVEL_BONUS = 3000
TIME_BONUS = 0.4
MAX_BOMB_ALLOWED = 2
