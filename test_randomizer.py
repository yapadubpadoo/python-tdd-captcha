import unittest
from randomizer import Randomizer


class TestRandomizer(unittest.TestCase):

	def test_get_pattern_should_return_1_or_2(self):
		randomizer = Randomizer()
		self.assertTrue(randomizer.get_pattern() >=1 and randomizer.get_pattern() <= 2)
		


