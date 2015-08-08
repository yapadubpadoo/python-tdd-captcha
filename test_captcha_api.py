import unittest
from app import app


class TestCaptchaAPI(unittest.TestCase):
	def test_root(self):
		self.app = app.test_client()
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual('Hello world!', response.data)

	def test_captcha(self):
		self.app = app.test_client()
		response = self.app.get('/captcha')
		self.assertEqual(response.status_code, 200)