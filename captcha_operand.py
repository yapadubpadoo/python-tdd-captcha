class CaptchaOperand:
	
	def __init__(self, operand):
		self.operand = str(operand)

	def get(self):
		return self.operand

	def to_string(self):
		return self.operand