import unittest

class SomeTestMethods(unittest.TestCase):
	def test_price_of_one_apple(self):
		scanner = Scanner()
		price_a = scanner.scan("Apple")
		self.assertEquals(price_a, 0.30)

	def test_price_of_one_biscuits(self):
		scanner = Scanner()
		price_b = scanner.scan("Biscuit")
		self.assertEquals(price_b, 0.50)

class Scanner(object):

	def scan(self, item):
		if item == "Apple":
			return 0.30
		elif item == "Biscuit":
			return 0.50
