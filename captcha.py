from captcha_operator import CaptchaOperator
from string_operand import StringOperand
from integer_operand import IntegerOperand

class Captcha:
	

	def __init__(self, captcha_type, left, operator, right):
		if captcha_type == 1:
			self.left = IntegerOperand(left)
			self.right = StringOperand(right)
		else:
			self.left = StringOperand(left)
			self.right = IntegerOperand(right)
		self.operator = CaptchaOperator(operator)

	def get_left(self):
		return self.left.to_string()

	def get_right(self):
		return self.right.to_string()

	def get_operator(self):
		return self.operator.to_string()
