def sum_series(n):
    total_sum = 0
    if isinstance(n, int):
        if n >= 0:
            for i in range(n // 2 + 1):
                total_sum += (n - 2*i)
            return total_sum
        else:
            return "Input must be a positive integer"
    else:
        return "Input must be an integer"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_series(6), 12)

if __name__ == '__main__':
    unittest.main()