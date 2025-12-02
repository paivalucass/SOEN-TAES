def fizz_buzz(n: int):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    def is_divisible_by_11_or_13(number):
        return (number % 11 == 0 or number % 13 == 0) and '7' in str(number)

    count = sum(1 for i in range(n) if is_divisible_by_11_or_13(i))
    return count
import unittest

class Test(unittest.TestCase):
    def test_fizz_buzz_50(self):
        self.assertEqual(fizz_buzz(50), 0)

    def test_fizz_buzz_78(self):
        self.assertEqual(fizz_buzz(78), 2)

    def test_fizz_buzz_79(self):
        self.assertEqual(fizz_buzz(79), 3)

if __name__ == '__main__':
    unittest.main()