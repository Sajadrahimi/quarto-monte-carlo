from game.Board import Board

from game.Totem import *

if __name__ == '__main__':
	board = Board()
	totems = []
	for i in range(16):
		totems.append(Totem("{0:04b}".format(i)))


