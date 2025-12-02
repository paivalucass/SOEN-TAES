def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return n == sqrt_n * sqrt_n
import unittest

# Function to check whether the given number is a perfect square or not
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()