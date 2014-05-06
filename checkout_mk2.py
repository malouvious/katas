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

	# def test_price_of_one_crisps(self):
	# 	scanner = Scanner()
	# 	price_c = scanner.scan("Crisps")
	# 	self.assertEquals(price_c, 1.00)

class Scanner(object):

	def __init__(self):
		self.prices = {"Apple": 0.30, "Biscuit": 0.50}

	def scan(self, item):
		return self.prices[item]