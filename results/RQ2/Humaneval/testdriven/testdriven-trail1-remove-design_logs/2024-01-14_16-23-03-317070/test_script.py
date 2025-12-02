def find_largest_prime_sum_of_digits(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    if not lst or any(num <= 0 for num in lst):
        return None

    prime_numbers = [num for num in lst if is_prime(num)]
    if not prime_numbers:
        return None
    max_prime = max(prime_numbers)
    return sum_of_digits(max_prime)
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(function_under_test([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)

    def test_2(self):
        self.assertEqual(function_under_test([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)

    def test_3(self):
        self.assertEqual(function_under_test([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)

    def test_4(self):
        self.assertEqual(function_under_test([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)

    def test_5(self):
        self.assertEqual(function_under_test([0,81,12,3,1,21]), 3)

    def test_6(self):
        self.assertEqual(function_under_test([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()