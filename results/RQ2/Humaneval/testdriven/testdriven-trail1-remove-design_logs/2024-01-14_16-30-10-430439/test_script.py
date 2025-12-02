def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count_of_numbers = 0
    for num in range(1, n):
        if (num % 11 == 0 or num % 13 == 0) and '7' in str(num):
            count_of_numbers += 1
    return count_of_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(50), 0)
        self.assertEqual(function_under_test(78), 2)
        self.assertEqual(function_under_test(79), 3)

if __name__ == '__main__':
    unittest.main()