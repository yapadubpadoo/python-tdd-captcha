import unittest
from captcha import Captcha


class TestFirstPatternLeftOperand(unittest.TestCase):
	def setUp(self):
		self.captcha = Captcha(1,1,1,1)

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
	def setUp(self):
		self.captcha = Captcha(1,1,1,1)

	def test_1_should_be_ONE(self):
		captcha = Captcha(2,1,1,1)
		self.assertEqual('ONE', captcha.getLeft())

	# def test_2_should_be_TWO(self):
	# 	captcha = Captcha(2,2,1,1)
	# 	self.assertEqual('TWO', captcha.getLeft())

	# def test_9_should_be_NINE(self):
	# 	captcha = Captcha(2,9,1,1)
	# 	self.assertEqual('NINE', captcha.getLeft())