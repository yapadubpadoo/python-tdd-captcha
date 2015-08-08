import unittest
from randomizer import Randomizer


class TestRandomizer(unittest.TestCase):

	def test_get_pattern_should_return_1_or_2(self):
		randomizer = Randomizer()
		self.assertTrue(randomizer.get_pattern() >=1 and randomizer.get_pattern() <= 2)

	def test_get_operator_should_return_between_1_and_3(self):
		randomizer = Randomizer()
		self.assertTrue(randomizer.get_operator() >=1 and randomizer.get_operator() <= 3)
	
	def test_get_number_should_return_between_1_and_9(self):
		randomizer = Randomizer()
		self.assertTrue(randomizer.get_operator() >=1 and randomizer.get_operator() <= 9)


