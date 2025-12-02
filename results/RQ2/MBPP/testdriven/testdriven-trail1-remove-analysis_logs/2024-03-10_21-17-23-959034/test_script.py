def get_max_sum(n):
    memo = {}

    def helper(n):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = max(helper(n//2) + helper(n//3) + helper(n//4) + helper(n//5), n)
        return memo[n]

    return helper(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()