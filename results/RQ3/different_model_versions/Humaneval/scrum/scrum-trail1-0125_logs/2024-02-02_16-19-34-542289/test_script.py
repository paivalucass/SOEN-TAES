def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def hex_key(num):
    primes_count = 0
    primes = ['2', '3', '5', '7', 'B', 'D']

    for digit in num:
        if digit.upper() in primes and is_prime(int(digit, 16)):
            primes_count += 1

    return primes_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('AB'), 1)
        self.assertEqual(function_under_test('1077E'), 2)
        self.assertEqual(function_under_test('ABED1A33'), 4)
        self.assertEqual(function_under_test('123456789ABCDEF0'), 6)
        self.assertEqual(function_under_test('2020'), 2)

if __name__ == '__main__':
    unittest.main()