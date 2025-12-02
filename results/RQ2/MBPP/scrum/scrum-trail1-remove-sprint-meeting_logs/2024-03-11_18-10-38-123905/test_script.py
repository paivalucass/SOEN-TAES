def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(0) == True
assert is_not_prime(1) == True
assert is_not_prime(2) == False
assert is_not_prime(17) == False
assert is_not_prime(1000000) == True
assert is_not_prime(3) == False
assert is_not_prime(4) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()