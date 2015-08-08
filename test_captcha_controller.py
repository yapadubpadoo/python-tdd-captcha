import unittest
import json
from captcha import Captcha
from captcha_controller import CaptchaController

class TestCaptchaController(unittest.TestCase):

	def test_get_json(self):
		captcha_controller = CaptchaController()
		captcha_controller.captcha = Captcha(1,1,1,1)
		self.assertTrue('{"left":"ONE", "operator":"+", "right":"1"}', captcha_controller.to_json())

	


