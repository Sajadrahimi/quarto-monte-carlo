from ai.agent import Node, RandomAgent
from game.Board import Board
import random
from game.Totem import *
from game.game import Game

if __name__ == '__main__':
	game = Game()
	node = Node(state=game)
	agent1 = RandomAgent(node)
	agent2 = RandomAgent(node)
	print('agent 1 is playing')
	new_board, playing_totem = agent1.do_action()
	print("NEW board", new_board)
	print("playing totem", playing_totem)
	game = new_board
	while game.status() == 'N/A':
		print('agent 2 is playing')
		agent2.root = Node(game)
		new_board, playing_totem = agent2.do_action(totem=playing_totem)
		game = new_board
		print("NEW board", new_board)
		print("playing totem", playing_totem)
		print('agent 1 is playing')
		agent1.root = Node(game)
		new_board, playing_totem = agent1.do_action(playing_totem)
		game = new_board
		print("NEW board", new_board)
		print("playing totem", playing_totem)
	print(game.status())
