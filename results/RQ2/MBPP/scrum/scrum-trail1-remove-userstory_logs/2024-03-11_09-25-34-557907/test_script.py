def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo = {0: 0, 1: 1}
        for i in range(2, n+1):
            memo[i] = memo[i-1] + 2*memo[i-2]
        return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()