import unittest

class SomeTestMethods(unittest.TestCase):
	def test_price_of_one_apple(self):
		scanner = Scanner()
		price_a = scanner.scan_apple()
		self.assertEquals(price_a, 0.30)

class Scanner(object):

	def scan_apple(self):
		return 0.30
