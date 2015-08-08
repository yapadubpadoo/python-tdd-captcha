import unittest
from captcha import Captcha


class TestFirstPatternLeftOperand(unittest.TestCase):

	def test_1_should_be_1(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual('1', captcha.getLeft())

	def test_2_should_be_2(self):
		captcha = Captcha(1,2,1,1)
		self.assertEqual('2', captcha.getLeft())

	def test_9_should_be_9(self):
		captcha = Captcha(1,9,1,1)
		self.assertEqual('9', captcha.getLeft())


class TestSecondPatternLeftOperand(unittest.TestCase):

	def test_1_should_be_ONE(self):
		first_pattern = 2
		focus = 1
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(first_pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('ONE', captcha.getLeft())

	def test_2_should_be_TWO(self):
		first_pattern = 2
		focus = 2
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(first_pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('TWO', captcha.getLeft())

	def test_5_should_be_FIVE(self):
		first_pattern = 2
		focus = 5
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(first_pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('FIVE', captcha.getLeft())

	def test_9_should_be_NINE(self):
		first_pattern = 2
		focus = 9
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(first_pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('NINE', captcha.getLeft())




