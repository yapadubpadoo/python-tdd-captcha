from captcha_operand import CaptchaOperand
class IntegerOperand(CaptchaOperand):
	def __init__(self, operand):
		CaptchaOperand.__init__(self, operand)

	def to_string(self):
		return str(self.operand)