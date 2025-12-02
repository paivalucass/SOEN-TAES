def sum_series(n):
    result = 0
    for i in range(n // 2 + 1):
        result += (n - 2 * i)
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_series(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()