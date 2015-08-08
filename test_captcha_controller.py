import unittest
import json
from captcha import Captcha
from captcha_controller import CaptchaController

class TestCaptchaController(unittest.TestCase):

	def test_get_json_pattern_1(self):
		captcha_controller = CaptchaController()
		captcha_controller.captcha = Captcha(1,1,1,1)
		self.assertTrue('{"left":"ONE", "operator":"+", "right":"1"}', captcha_controller.to_json())

	def test_get_json_pattern_2(self):
		captcha_controller = CaptchaController()
		captcha_controller.captcha = Captcha(2,1,2,5)
		self.assertTrue('{"left":"1", "operator":"x", "right":"FIVE"}', captcha_controller.to_json())

	


