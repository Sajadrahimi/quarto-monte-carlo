import random
from copy import deepcopy

from game.Board import Board
from game.Totem import Totem
from game.game import Game


class Node:
	def __init__(self, state: Game, parent=None):
		self.state = state
		self.parent = parent
		self.put_actions = []
		self.choose_actions = []
		self.visits = 1
		self.reward = 0.0

		for t in self.state.totems:
			for (i, j) in self.state.board.get_available():
				self.put_actions.append(deepcopy(state).put_totem(t, i, j))

	def update(self, reward):
		self.reward += reward
		self.visits += 1

	def fully_expanded(self):
		return len(self.state.totems) == 0


class Agent:

	def __init__(self, root: Node):
		self.root = root

	def totem_set_action(self, totem: Totem):
		pass

	def totem_choose_action(self):
		pass

	def do_action(self, totem: Totem = None) -> tuple:
		if totem:
			return self.totem_set_action(totem), self.totem_choose_action()
		return self.root.state, self.totem_choose_action()


class MCTSAgent(Agent):
	pass


class RandomAgent(Agent):

	def totem_set_action(self, totem):
		# print("in set totem")
		state_copy = deepcopy(self.root.state)
		# print("state_copy", state_copy)
		(i, j) = random.sample(state_copy.board.get_available(), 1)[0]
		state_copy = state_copy.put_totem(totem, i, j)
		# print("after putting", state_copy)
		self.root = Node(state_copy,
						 parent=self.root)
		return self.root.state

	def totem_choose_action(self):
		return random.sample(self.root.state.totems, 1)[0]
