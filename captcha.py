class Captcha:
	number_map = {
		'1': 'ONE'
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