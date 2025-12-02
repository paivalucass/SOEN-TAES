def catalan_number(num):
    # Implementing memoization
    memo = {}

    def calculate_catalan(n):
        if type(n) != int or n < 0:
            return "Invalid input"
        if n <= 1:
            return 1

        if n in memo:
            return memo[n]

        res = 0
        for i in range(n):
            res += calculate_catalan(i) * calculate_catalan(n - i - 1)

        memo[n] = res
        return res

    return calculate_catalan(num)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()