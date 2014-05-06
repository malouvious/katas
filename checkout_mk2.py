import unittest

class SomeTestMethods(unittest.TestCase):
	def test_price_of_one_apple(self):
		prices = {"Apple": 0.30, "Biscuit": 0.50}
		scanner = Scanner(prices)
		price_a = scanner.scan("Apple")
		self.assertEqual(price_a, 0.30)

	def test_price_of_one_biscuits(self):
		prices = {"Apple": 0.30, "Biscuit": 0.50}
		scanner = Scanner(prices)
		price_b = scanner.scan("Biscuit")
		self.assertEqual(price_b, 0.50)

	# def test_price_of_one_crisps(self):
	# 	scanner = Scanner()
	# 	price_c = scanner.scan("Crisps")
	# 	self.assertEquals(price_c, 1.00)

class Scanner(object):

	def __init__(self, prices):
		self.prices = prices

	def scan(self, item):
		return self.prices[item]