def sum_series(n):
    total_sum = 0
    for i in range((n+2) // 2):
        total_sum += n - 2*i
    return total_sum

assert sum_series(6) == 12
assert sum_series(3) == 4
assert sum_series(7) == 16
assert sum_series(0) == 0
assert sum_series(1) == 1
assert sum_series(-6) == -6
import unittest

class Test(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()