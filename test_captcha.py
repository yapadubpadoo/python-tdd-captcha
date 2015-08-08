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

	def test_2_should_be_TWO(self):
		pattern = 2
		focus = 2
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('TWO', captcha.getLeft())

	def test_5_should_be_FIVE(self):
		pattern = 2
		focus = 5
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('FIVE', captcha.getLeft())

	def test_9_should_be_NINE(self):
		pattern = 2
		focus = 9
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('NINE', captcha.getLeft())

class TestFirstPatternRightOperand(unittest.TestCase):
	def test_1_should_be_1(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 1
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('1', captcha.getRight())

	def test_2_should_be_2(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 2
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('2', captcha.getRight())

	def test_9_should_be_9(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 9
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('9', captcha.getRight())

# class TestSecondPatternRightOperand(unittest.TestCase):



