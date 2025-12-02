def is_nonagonal(n):
    if not isinstance(n, int) or n < 1:
        return "Error: Invalid input, n must be a positive integer"

    memo = {}

    def calculate_nonagonal(m):
        if m in memo:
            return memo[m]
        result = m * (7 * m - 5) / 2
        memo[m] = result
        return result

    return calculate_nonagonal(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()