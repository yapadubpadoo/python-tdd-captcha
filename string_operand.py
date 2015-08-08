from captcha_operand import CaptchaOperand

class StringOperand(CaptchaOperand):
	number_map = {
		'1': 'ONE',
		'2': 'TWO',
		'3': 'THREE',
		'4': 'FOUR',
		'5': 'FIVE',
		'6': 'SIX',
		'7': 'SEVEN',
		'8': 'EIGHT',
		'9': 'NINE',
	}

	def __init__(self, operand):
		CaptchaOperand.__init__(self, operand)

	def to_string(self):
		return self.number_map[self.operand]