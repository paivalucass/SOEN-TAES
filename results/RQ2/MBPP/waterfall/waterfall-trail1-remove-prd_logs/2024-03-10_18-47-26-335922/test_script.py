def jacobsthal_num(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    memo = {0: 0, 1: 1}
    
    def jacobsthal_helper(n):
        if n not in memo:
            memo[n] = jacobsthal_helper(n-1) + 2 * jacobsthal_helper(n-2)
        return memo[n]
    
    return jacobsthal_helper(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()