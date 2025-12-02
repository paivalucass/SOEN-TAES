def sum_digits(n):
    total_sum = 0
    
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    elif n == 0:
        return 0
    
    for digit in str(abs(n)):
        if digit.isdigit():
            total_sum += int(digit)
    
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()