def sum_digits(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid Input"

    total = 0
    for digit in str(n):
        total += int(digit)
    
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()