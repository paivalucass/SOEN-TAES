def is_not_prime(n):
    if not isinstance(n, int):
        return "Invalid Input"
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()