def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    length = len(string)
    return is_prime(length) if length > 1 else False

# Test cases
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False
print(prime_length(''))  # False
print(prime_length('a'))  # False
print(prime_length('a'*1001))  # False
import unittest

class Test(unittest.TestCase):
    def test_prime_length(self):
        self.assertEqual(prime_length('Hello'), True)
        self.assertEqual(prime_length('abcdcba'), True)
        self.assertEqual(prime_length('kittens'), True)
        self.assertEqual(prime_length('orange'), False)

if __name__ == '__main__':
    unittest.main()