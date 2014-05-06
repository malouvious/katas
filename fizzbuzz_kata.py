import unittest

class SomeTests(unittest.TestCase):

	def test_multiple_of_three_returns_Fizz(self):
		self.assertEqual(fizz_or_buzz(6), "Fizz")

	def test_multiple_of_five_returns_Buzz(self):
		self.assertEqual(fizz_or_buzz(10), "Buzz")

	def test_multiple_of_three_and_five_returns_FizzBuzz(self):
		self.assertEqual(fizz_or_buzz(15), "FizzBuzz")

	def test_non_fizzbuzz_value_gives_value(self):
		self.assertEqual(fizz_or_buzz(7), 7)

	def test_fizzbuzz_sequence_upto_15(self):
		sequence = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
		self.assertListEqual(fizzbuzz_list(15), sequence)


def fizz_or_buzz(value):
	if value % 3 == 0 and value % 5 == 0:
		return "FizzBuzz"
	elif value % 3 == 0:
		return "Fizz"
	elif value % 5 == 0:
		return "Buzz"
	else:
		return value

def fizzbuzz_list(value):
	sequence = []
	for i in range(value):
		sequence.append(fizz_or_buzz(i+1))
	return sequence

if __name__ == "__main__":
	unittest.main()