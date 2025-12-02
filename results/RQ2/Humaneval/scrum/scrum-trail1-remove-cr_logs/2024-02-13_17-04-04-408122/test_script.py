def prime_length(string):
    if len(string) < 2:
        return False
    for i in range(2, int(len(string) ** 0.5) + 1):
        if len(string) % i == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_prime_length(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))
        self.assertFalse(prime_length('orange'))

if __name__ == '__main__':
    unittest.main()