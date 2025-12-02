def get_max_sum(n):
    memo = {}

    def helper(num):
        if num <= 1:
            return num
        
        if num in memo:
            return memo[num]

        memo[num] = max(num, helper(num//2) + helper(num//3) + helper(num//4) + helper(num//5))
        return memo[num]
    
    return helper(n)
import unittest

class Test(unittest.TestCase):
    def test_get_max_sum(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()