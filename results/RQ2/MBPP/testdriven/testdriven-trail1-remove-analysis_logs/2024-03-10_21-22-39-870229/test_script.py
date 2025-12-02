def sum_digits(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    else:
        return sum(int(x) for x in str(n))

# Test cases
print(sum_digits(345))  # Expected output: 12
print(sum_digits(7))    # Expected output: 7
print(sum_digits(0))    # Expected output: 0
print(sum_digits(-123))  # Expected output: Invalid Input
print(sum_digits(999999))  # Expected output: 54
print(sum_digits(345))  # Expected output: 12
print(sum_digits("abc"))  # Expected output: Invalid Input
print(sum_digits(1000000000000000))  # Expected output: Invalid Input
import unittest

class Test(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()