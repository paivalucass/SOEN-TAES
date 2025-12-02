def sum_odd(l, r):
    if l < 0 or r < 0:
        raise ValueError("Input values cannot be negative")
    if l % 1 != 0 or r % 1 != 0:
        raise ValueError("Input values must be natural numbers")

    if l > r:
        raise ValueError("Invalid range: l cannot be greater than r")

    sum_of_odd = 0
    for number in range(l, r+1):
        if number % 2 != 0:
            sum_of_odd += number
    return sum_of_odd

assert sum_odd(2,5) == 8
import unittest

class Test(unittest.TestCase):
    def test_sum_odd(self):
        self.assertEqual(sum_odd(2,5), 8)

if __name__ == '__main__':
    unittest.main()