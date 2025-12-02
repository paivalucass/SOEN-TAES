def sum_digits(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input integer must be non-negative")
    
    # Extract individual digits using modulo and division operations
    # Sum up the extracted digits and return the result
    return sum(int(digit) for digit in str(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()