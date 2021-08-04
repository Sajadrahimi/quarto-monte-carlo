from game.Totem import Totem, are_similar


class Board:
	N: int = 4
	grid: list = []
	empty_cells_cache = []
	present_totems = []

	def __init__(self, N: int = None):
		if N:
			self.N = N
		self.grid = [[None for _ in range(self.N)] for _ in range(self.N)]

		# set all cells as empty, Not so memory efficient!
		for i in range(self.N):
			for j in range(self.N):
				if self.is_empty(i, j):
					self.empty_cells_cache.append((i, j))

	def is_empty(self, row: int, col: int) -> bool:
		""" Checks if a certain cell is empty or not. """
		assert row in range(self.N), "row out of range"
		assert col in range(self.N), "col out of range"
		return self.grid[row][col] is None

	def get_available(self) -> list:
		""" returns a list of all empty cells"""
		return self.empty_cells_cache

	def is_allowed(self, totem: Totem) -> bool:
		return totem not in self.present_totems

	def get_totem(self, row: int, col: int) -> Totem:
		assert row in range(self.N), "row out of range"
		assert col in range(self.N), "col out of range"
		return self.grid[row][col]

	def set_totem(self, totem: Totem, row: int, col: int) -> bool:
		""" If allowed, Sets a totem in a cell, and updates empty cells list cache."""
		assert row in range(self.N), "row out of range"
		assert col in range(self.N), "col out of range"
		if self.is_empty(row, col):
			self.grid[row][col] = totem
			self.empty_cells_cache.remove([row, col])
			self.present_totems.append(totem)
			return True
		return False

	def get_row(self, i: int) -> list:
		assert i in range(self.N), "i out of range"
		return [self.get_totem(i, j) for j in range(self.N)]

	def get_col(self, j: int) -> list:
		assert j in range(self.N), "col out of range"
		return [self.get_totem(i, j) for i in range(self.N)]

	def get_diag(self) -> list:
		return [self.get_totem(i, i) for i in range(self.N)]

	def get_adiag(self) -> list:
		return [self.get_totem(self.N - (i + 1), i) for i in range(self.N)]

	def status(self):
		for i in range(self.N):
			if are_similar(self.get_row(i)):
				return 'match in row %d' % i
			if are_similar(self.get_col(i)):
				return 'match in column %d' % i
		if are_similar(self.get_diag()):
			return 'match in main diagonal'
		elif are_similar(self.get_adiag()):
			return 'match in anti diagonal'

		elif not self.empty_cells_cache:
			return 'tie'

		return 'N/A'

	def __repr__(self):
		return str(self.grid)
