def sum_series(n):
    total = 0
    for i in range(n // 2):
        total += n - 2 * i
    return total

assert sum_series(6) == 12
import unittest

class Test(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()