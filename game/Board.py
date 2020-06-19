from game.Totem import Totem


class Board:
	grid = None

	def __init__(self):
		self.grid = [[None for _ in range(4)] for _ in range(4)]

	def is_empty(self, i: int, j: int):
		assert i in range(4), "i out of range"
		assert j in range(4), "j out of range"
		return self.grid[i][j] is None

	def get_available(self):
		free = []
		for i in range(4):
			for j in range(4):
				if self.is_empty(i, j):
					free.append((i, j))
		return free

	def is_allowed(self, totem: Totem):
		for i in range(4):
			for j in range(4):
				if self.get_totem(i, j) == totem:
					return False
		return True

	def get_totem(self, i: int, j: int):
		assert i in range(4), "i out of range"
		assert j in range(4), "j out of range"
		return self.grid[i][j]

	def get_row(self, i: int):
		assert i in range(4), "i out of range"
		return [self.get_totem(i, j) for j in range(4)]

	def get_col(self, j: int):
		assert j in range(4), "j out of range"
		return [self.get_totem(i, j) for i in range(4)]

	def get_diag(self):
		return [self.get_totem(i, i) for i in range(4)]

	def get_adiag(self):
		return [self.get_totem(4 - (i + 1), i) for i in range(4)]
