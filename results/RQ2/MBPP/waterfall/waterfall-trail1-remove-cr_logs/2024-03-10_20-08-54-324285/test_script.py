def sum_digits(n):
    if n < 0:
        raise ValueError("Input integer must be non-negative")

    running_sum = 0
    while n > 0:
        digit = n % 10
        running_sum += digit
        n //= 10

    return running_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()