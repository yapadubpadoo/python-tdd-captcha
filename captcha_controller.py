from captcha import Captcha
from randomizer import Randomizer

class CaptchaController:
	def __init__(self):
		randomizer = Randomizer()
		pattern = randomizer.get_pattern()
		left = randomizer.get_number()
		operator = randomizer.get_operator()
		right = randomizer.get_number()
		self.captcha = Captcha(pattern, left, operator, right)

	def to_json(self):
		left = self.captcha.get_left()
		operator = self.captcha.get_operator()
		right = self.captcha.get_right()
		json = '{"left":"%s", "operator":"%s", "right":"%s"}'  % (left, operator, right)
		return json

