import unittest
from captcha import Captcha
from captcha_operator import CaptchaOperator


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

class TestSecondPatternRightOperand(unittest.TestCase):
	def test_3_should_be_THREE(self):
		pattern = 2
		dummy_left = 2
		dummy_operator = 1
		focus = 3
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('THREE', captcha.getRight())

	def test_6_should_be_SIX(self):
		pattern = 2
		dummy_left = 5
		dummy_operator = 1
		focus = 6
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('SIX', captcha.getRight())

	def test_7_should_be_SEVEN(self):
		pattern = 2
		dummy_left = 9
		dummy_operator = 1
		focus = 7
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('SEVEN', captcha.getRight())

class TestOperator(unittest.TestCase):
	def test_1_should_return_ADD_operator(self):
		focus = 1
		oprator = CaptchaOperator(operator_type = focus)
		self.assertEqual('+', oprator.toString())

	def test_2_should_return_MULTIPLY_operator(self):
		focus = 2
		oprator = CaptchaOperator(operator_type = focus)
		self.assertEqual('x', oprator.toString())

	def test_3_should_return_MINUS_operator(self):
		focus = 3
		oprator = CaptchaOperator(operator_type = focus)
		self.assertEqual('-', oprator.toString())
	

