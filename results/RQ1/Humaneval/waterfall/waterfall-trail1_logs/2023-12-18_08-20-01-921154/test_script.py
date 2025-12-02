def prime_length(string):
    if len(string) < 2:
        return False
    
    for i in range(2, int(len(string)**0.5) + 1):
        if len(string) % i == 0:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test_prime_length(self):
        self.assertEqual(prime_length('Hello'), True)
        self.assertEqual(prime_length('abcdcba'), True)
        self.assertEqual(prime_length('kittens'), True)
        self.assertEqual(prime_length('orange'), False)

if __name__ == '__main__':
    unittest.main()