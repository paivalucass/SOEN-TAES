def sum_odd(l, r):
    if not isinstance(l, int) or not isinstance(r, int) or l < 0 or r < 0:
        raise ValueError("l and r should be positive integers")

    odd_sum = 0
    for i in range(l, r+1):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()