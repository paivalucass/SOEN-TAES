def sum_odd(n, l, r):
    if not all(isinstance(param, int) and param > 0 for param in [n, l, r]):
        raise ValueError("Input parameters n, l, and r must be positive integers")
    odd_sum = 0
    for num in range(l, r+1):
        if num % 2 != 0:
            odd_sum += num
    return odd_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()