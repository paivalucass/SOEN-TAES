def get_max_sum(n):
    if n <= 0:
        return "Invalid input"
    memoization = {}
    def helper(m):
        if m <= 0:
            return 0
        if m in memoization:
            return memoization[m]
        memoization[m] = max(helper(m//2) + helper(m//3) + helper(m//4) + helper(m//5), m)
        return memoization[m]

    return helper(n)

assert get_max_sum(60) == 106
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()