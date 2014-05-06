import unittest

class FizzBuzzTests(unittest.TestCase):

	def test_multiple_of_three_returns_Fizz(self):
		fizz1 = FizzBuzz()
		self.assertEqual(fizz1.getResult(6), "Fizz")

	def test_multiple_of_five_returns_Buzz(self):
		fizz1 = FizzBuzz()
		self.assertEqual(fizz1.getResult(10), "Buzz")

	def test_multiple_of_three_and_five_returns_FizzBuzz(self):
		fizz1 = FizzBuzz()
		self.assertEqual(fizz1.getResult(15), "FizzBuzz")

	def test_non_fizzbuzz_value_gives_value(self):
		fizz1 = FizzBuzz()
		self.assertEqual(fizz1.getResult(7), 7)

	def test_fizzbuzz_sequence_upto_15(self):
		fizz1 = FizzBuzz()
		sequence = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
		self.assertListEqual(fizz1.getList(15), sequence)

	def test_weird_shit(self):
		fizz1 = FizzBuzz()
		with self.assertRaises(AssertionError):
			fizz1.getResult(-1)
		with self.assertRaises(AssertionError):
			fizz1.getResult(15.5)

class FizzBuzz(object):
	
	def getList(self, number): # Generate list
		sequence = []
		for i in range(1, number+1):
			sequence.append(self.getResult(i))
		return sequence

	def getResult(self, value): # Fizz, Buzz, or number

		assert value > 0
		assert type(value) is int

		if value % 3 == 0 and value % 5 == 0:
			return "FizzBuzz"
		elif value % 3 == 0:
			return "Fizz"
		elif value % 5 == 0:
			return "Buzz"
		else:
			return value

class FizzBuzzOther(FizzBuzz):
	def getList(self, numberAsAString):
		number = int(numberAsAString)
		return super(FizzBuzzOther, self).getList(number)


if __name__ == "__main__":
	#unittest.main()

	o = FizzBuzzOther()
	print(o.getList("15"))