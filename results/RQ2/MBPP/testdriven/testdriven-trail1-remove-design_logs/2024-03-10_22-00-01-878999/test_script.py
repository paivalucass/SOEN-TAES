def sum_series(n):
    total_sum = 0
    for i in range(0, n // 2 + 1):
        total_sum += n - 2 * i
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()