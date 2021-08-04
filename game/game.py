from game.Board import Board
from game.Totem import Totem, are_similar


class Game:
	N: int = 4

	def __init__(self, N: int = None):
		self.board = Board(N)
		N = 4 if not N else N
		self.totems = [Totem("{0:04b}".format(i)) for i in range(4 * N)]

	def put_totem(self, totem: Totem, i: int, j: int):
		try:
			if self.board.set_totem(totem, i, j):
				self.totems.remove(totem)
				return True
			return False
		except Exception as e:
			print(e)

	def status(self):
		return self.board.status()