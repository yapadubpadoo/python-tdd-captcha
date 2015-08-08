class Captcha:
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

	operator_symbol = {
	'1': '+',
	'2': 'x',
	'3': '-'
	}
	
	def __init__(self, captcha_type, left, operator, right):
		self.captcha_type = captcha_type
		self.left = str(left)
		self.operator = str(operator)
		self.right = str(right)

	def getLeft(self):
		if(self.captcha_type == 2):
			return self.number_map[self.left]
		else:
			return self.left

	def getRight(self):
		if(self.captcha_type == 2):
			return self.number_map[self.right]
		else:
			return self.right

	def getOperator(self):
		return self.operator_symbol[self.operator]