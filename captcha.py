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
	def __init__(self, captcha_type, left, oprator, right):
		self.captcha_type = captcha_type
		self.left = str(left)
		self.operator = str(left)
		self.right = str(left)

	def getLeft(self):
		if(self.captcha_type == 2):
			return self.number_map[self.left]
		else:
			return self.left