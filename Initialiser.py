from Board import Board

def placeWalls(BombermanBoard):
	for i in range(0, BombermanBoard.height):
		BombermanBoard.arena.append([])
		for j in range(0, BombermanBoard.width):
			BombermanBoard.arena[i].append(' ')

	for i in range(0, BombermanBoard.height):
		BombermanBoard.arena[i][BombermanBoard.width - 1] = '#'
		BombermanBoard.arena[i][0] = '#'

		for i in range(0, BombermanBoard.width):
			BombermanBoard.arena[BombermanBoard.height - 1][i] = '#'
			BombermanBoard.arena[0][i] = '#'

	for i in range(2, BombermanBoard.height):
		for j in range(2, BombermanBoard.width):
			if i % 2 == 0 and j % 2 == 0:
				BombermanBoard.arena[i][j] = '#'
	pass

def loadBoard():
	BombermanBoard = Board()
	placeWalls(BombermanBoard)
	print(BombermanBoard.scaledBoard())
loadBoard()
