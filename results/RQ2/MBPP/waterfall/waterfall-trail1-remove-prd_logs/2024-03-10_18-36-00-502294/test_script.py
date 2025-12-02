def get_max_sum(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n <= 0:
        return 0
    elif n <= 5:
        return n

    memo = {}
    
    def helper(num):
        if not isinstance(num, int) or num < 0:
            raise ValueError("Input must be a non-negative integer")
            
        if num in memo:
            return memo[num]
        if num <= 0:
            result = 0
        elif num <= 5:
            result = num
        else:
            result = max(num, helper(num//2) + helper(num//3) + helper(num//4) + helper(num//5))
        memo[num] = result
        return result

    return helper(n)

assert get_max_sum(60) == 106
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()