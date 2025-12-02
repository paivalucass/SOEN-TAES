def find_lucas(n):
    if n <= 0:
        return "Input validation error"
    
    # Using memoization to improve performance
    memo = {0: 2, 1: 1}
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()