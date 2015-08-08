import unittest
import json
from captcha import Captcha
from randomizer import Randomizer
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

	
	def test_get_json_with_stub_randomizer(self):
		stub_randomizer = Randomizer()
		def get_pattern():
			return 1
		def get_number():
			return 1
		def get_operator():
			return 1
		captcha_controller = CaptchaController()
		stub_randomizer.get_pattern = get_pattern
		stub_randomizer.get_number = get_number
		stub_randomizer.get_operator = get_operator
		captcha_controller.randomizer = stub_randomizer
		self.assertTrue('{"left":"ONE", "operator":"+", "right":"1"}', captcha_controller.to_json())
