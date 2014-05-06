import unittest

class SomeTests(unittest.TestCase):

	def test_scan_item_equals_item_price(self):
		blcd_price = 60
		checkout = Checkout({blcd: blcd_price})
		checkout.scan(blcd)
		price_of_b = checkout.total()
		self.assertEqual(price_of_b, blcd_price)

	def test_two_Apples_costs_100(self):
		apple_price = 50
		checkout = Checkout({apple: apple_price})
		checkout.scan(apple)
		checkout.scan(apple)
		price_of_2_a = checkout.total()
		self.assertEqual(price_of_2_a, apple_price * 2)

apple = "A"
blcd = "B"

class Checkout(object):

	def __init__(self, prices):
		self._total = 0
		self._prices = prices

	def scan(self, item):
		self._total += self._prices[item]

	def total(self):
		return self._total


if __name__ == "__main__":
	unittest.main()