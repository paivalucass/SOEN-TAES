def get_max_sum(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = {}
    def calculate_max_sum(n):
        if n in memo:
            return memo[n]
        if n < 2:
            return n
        memo[n] = max((calculate_max_sum(n//2) + calculate_max_sum(n//3) + calculate_max_sum(n//4) + calculate_max_sum(n//5)), n)
        return memo[n]
    result = calculate_max_sum(n)
    if result == n:
        return "Error"
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()