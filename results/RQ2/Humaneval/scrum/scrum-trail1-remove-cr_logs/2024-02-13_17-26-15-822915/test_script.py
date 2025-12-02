def digits(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"
    
    odd_digits = [int(d) for d in str(n) if int(d) % 2 != 0]
    
    if not odd_digits:
        return 0
    
    product = 1
    for digit in odd_digits:
        product *= digit
    
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

if __name__ == '__main__':
    unittest.main()