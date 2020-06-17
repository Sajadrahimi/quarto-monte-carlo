from functools import reduce
from operator import iand, invert, inv, neg
from typing import List


class Totem:
	"""
		the type is represented by a 4 bit binary number in which
		first bit: is tall
		second bit: is white
		third bit: is square
		forth bit: is hallow
		e.g. a Tall Black Hallow Round totem will be represented as 1001

		This representation will help to evaluate win or lose situation in more efficient way
	"""
	totem_type = str

	def __init__(self, totem_type):
		self.totem_type = totem_type

	def __str__(self):
		return "%s" % self.totem_type

	def __eq__(self, other):
		return self.totem_type == other.totem_type


def are_similar(totems: List[Totem]):
	assert len(totems) > 1, "at least two totems are required"

	for i in range(4):
		if reduce(iand, [~(int(x.totem_type[i]) - 2) for x in totems]) + reduce(iand, [int(x.totem_type[i]) for x in totems]) == 1:
			return True
	return False
