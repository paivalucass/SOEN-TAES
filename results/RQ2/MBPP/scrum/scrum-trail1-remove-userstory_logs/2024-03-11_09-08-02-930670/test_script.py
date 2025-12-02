def get_max_sum(n):
    memo = {}

    def calculate_max_sum(n):
        if n in memo:
            return memo[n]

        if n <= 1:
            result = n
        else:
            result = max(n, calculate_max_sum(n//2) + calculate_max_sum(n//3) + calculate_max_sum(n//4) + calculate_max_sum(n//5))

        memo[n] = result
        return result

    return calculate_max_sum(n)
import unittest

class Test(unittest.TestCase):
    def test_get_max_sum(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()