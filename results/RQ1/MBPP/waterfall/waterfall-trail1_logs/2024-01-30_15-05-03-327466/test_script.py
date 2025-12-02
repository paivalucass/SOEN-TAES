def jacobsthal_num(n): 
    '''Function to find the nth Jacobsthal number using memoization'''
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev1 = 0
    prev2 = 1
    for i in range(2, n+1):
        current = prev1 * 2 + prev2
        prev1, prev2 = prev2, current
    
    return current

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()