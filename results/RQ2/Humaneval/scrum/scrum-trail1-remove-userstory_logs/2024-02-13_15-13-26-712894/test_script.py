def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_length(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    length = len(string)
    if length < 2:
        return False
    
    return is_prime(length)
import unittest

class Test(unittest.TestCase):
    def test_prime_length(self):
        self.assertEqual(prime_length('Hello'), True)
        self.assertEqual(prime_length('abcdcba'), True)
        self.assertEqual(prime_length('kittens'), True)
        self.assertEqual(prime_length('orange'), False)

if __name__ == '__main__':
    unittest.main()