import unittest

class SomeTestMethods(unittest.TestCase):
	def test_price_of_an_item(self):
		prices = {"Apple": 0.30}
		scanner = Scanner(prices)
		price_a = scanner.scan("Apple")
		self.assertEqual(price_a, 0.30)

	def test_price_of_two_apples(self):
		prices = {"Apple": 0.30}
		scanner = Scanner(prices)
		price_a = scanner.scan("Apple")
		price_a += scanner.scan("Apple")
		self.assertEqual(price_a, 0.60)

	# def test_two_apples_offer(self):
	# 	price_of_2_a = 0.30
	# 	self.assertEqual(price_of_2_a, 0.30)

class Scanner(object):

	def __init__(self, prices):
		self.prices = prices

	def scan(self, item):
		return self.prices[item]