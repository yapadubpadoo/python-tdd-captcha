import random

class Randomizer():
	def get_pattern(self):
		return random.randrange(1,2)

	def get_operator(self):
		return random.randrange(1,3)

	def get_number(self):
		return random.randrange(1,9)