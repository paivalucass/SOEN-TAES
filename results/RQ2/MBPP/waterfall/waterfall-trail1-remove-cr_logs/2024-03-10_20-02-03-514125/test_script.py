def get_max_sum(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    memo = {}
    
    def max_sum_helper(n):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        max_sum = max(max_sum_helper(n//2) + max_sum_helper(n//3) + max_sum_helper(n//4) + max_sum_helper(n//5), n)
        memo[n] = max_sum
        return max_sum
    
    return max_sum_helper(n)
import unittest

class Test(unittest.TestCase):
    def test_get_max_sum(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()