from game.Board import Board
from game.Totem import Totem, are_similar


class Game:

	def __init__(self):
		self.board = Board()
		self.totems = [Totem("{0:04b}".format(i)) for i in range(16)]

	def put_totem(self, totem: Totem, i: int, j: int):
		assert i in range(4), "i out of range"
		assert j in range(4), "j out of range"
		try:
			if self.board.is_empty(i, j):
				self.board.grid[i][j] = totem
				self.totems.remove(totem)
				return self
		except Exception as e:
			print(e)

	def status(self):
		for i in range(4):
			if are_similar(self.board.get_row(i)):
				return 'match in row %d' % i
			if are_similar(self.board.get_col(i)):
				return 'match in column %d' % i
		if are_similar(self.board.get_diag()):
			return 'match in main diagonal'
		if are_similar(self.board.get_adiag()):
			return 'match in anti diagonal'

		if not self.totems:
			return 'tie'

		return 'N/A'

	def __repr__(self):
		return str(self.board.grid)
