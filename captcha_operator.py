class CaptchaOperator:
	operator_symbol = {
		'1': '+',
		'2': 'x',
		'3': '-'
	}
	def __init__(self, operator_type):
		self.operator_type = str(operator_type)

	def to_string(self):
		return self.operator_symbol[self.operator_type]