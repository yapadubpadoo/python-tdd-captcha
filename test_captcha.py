import unittest
from captcha import Captcha
from captcha_operator import CaptchaOperator
from string_operand import StringOperand
from integer_operand import IntegerOperand


class TestFirstPatternLeftOperand(unittest.TestCase):

	def test_1_should_be_1(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual('1', captcha.get_left())

	def test_2_should_be_2(self):
		captcha = Captcha(1,2,1,1)
		self.assertEqual('2', captcha.get_left())

	def test_9_should_be_9(self):
		captcha = Captcha(1,9,1,1)
		self.assertEqual('9', captcha.get_left())


class TestSecondPatternLeftOperand(unittest.TestCase):
	def test_2_should_be_TWO(self):
		pattern = 2
		focus = 2
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('TWO', captcha.get_left())

	def test_5_should_be_FIVE(self):
		pattern = 2
		focus = 5
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('FIVE', captcha.get_left())

	def test_9_should_be_NINE(self):
		pattern = 2
		focus = 9
		dummy_operator = 1
		dummy_right = 1
		captcha = Captcha(pattern, focus, dummy_operator, dummy_right)
		self.assertEqual('NINE', captcha.get_left())

class TestFirstPatternRightOperand(unittest.TestCase):
	def test_1_should_be_ONE(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 1
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('ONE', captcha.get_right())

	def test_2_should_be_TWO(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 2
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('TWO', captcha.get_right())

	def test_9_should_be_NINE(self):
		pattern = 1
		dummy_left = 9
		dummy_operator = 1
		focus = 9
		captcha = Captcha(pattern, dummy_left, dummy_operator, focus)
		self.assertEqual('NINE', captcha.get_right())

class TestSecondPatternRightOperand(unittest.TestCase):
	def test_3_should_be_3(self):
		pattern = 2
		dummy_left = 2
		dummy_operator = 1
		captcha = Captcha(pattern, dummy_left, dummy_operator, 3)
		self.assertEqual('3', captcha.get_right())

	def test_6_should_be_6(self):
		pattern = 2
		dummy_left = 5
		dummy_operator = 1
		captcha = Captcha(pattern, dummy_left, dummy_operator, 6)
		self.assertEqual('6', captcha.get_right())

	def test_7_should_be_7(self):
		pattern = 2
		dummy_left = 9
		dummy_operator = 1
		captcha = Captcha(pattern, dummy_left, dummy_operator, 7)
		self.assertEqual('7', captcha.get_right())

class TestCaptchaGetOperator(unittest.TestCase):
	def test_1_should_return_ADD_operator(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual('+', captcha.get_operator())

	def test_2_should_return_MULTIPLY_operator(self):
		captcha = Captcha(1,1,2,1)
		self.assertEqual('x', captcha.get_operator())

	def test_3_should_return_MINUS_operator(self):
		captcha = Captcha(1,1,3,1)
		self.assertEqual('-', captcha.get_operator())


class TestOperator(unittest.TestCase):
	def test_1_should_return_ADD_operator(self):
		operator = CaptchaOperator(operator_type = 1)
		self.assertEqual('+', operator.to_string())

	def test_2_should_return_MULTIPLY_operator(self):
		operator = CaptchaOperator(operator_type = 2)
		self.assertEqual('x', operator.to_string())

	def test_3_should_return_MINUS_operator(self):
		operator = CaptchaOperator(operator_type = 3)
		self.assertEqual('-', operator.to_string())


class TestStringOperand(unittest.TestCase):
	def test_1_should_return_ONE(self):
		focus = 1
		string_operand = StringOperand(operand = focus)
		self.assertEqual('ONE', string_operand.to_string())

	def test_9_should_return_NINE(self):
		focus = 9
		string_operand = StringOperand(operand = focus)
		self.assertEqual('NINE', string_operand.to_string())

class TestIntegerOperand(unittest.TestCase):
	def test_1_should_return_1(self):
		focus = 1
		string_operand = IntegerOperand(focus)
		self.assertEqual('1', string_operand.to_string())

	def test_9_should_return_9(self):
		focus = 9
		string_operand = IntegerOperand(focus)
		self.assertEqual('9', string_operand.to_string())
	



