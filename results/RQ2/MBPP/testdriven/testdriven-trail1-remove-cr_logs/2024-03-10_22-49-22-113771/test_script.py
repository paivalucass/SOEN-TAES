def is_nonagonal(n):
    '''
    Write a function to find the nth nonagonal number.
    
    This function should take an integer n as input and return the nth nonagonal number.
    
    Input Range:
    - n should be a positive integer
    
    Error Handling:
    - If n is not a positive integer, the function should raise a ValueError
    
    Algorithm:
    - The nonagonal number can be calculated using the formula: n * (7*n - 5) / 2
    
    Detailed Comments:
    - The formula n * (7n - 5) / 2 is derived from the pattern of nonagonal numbers, where each nonagonal number is the product of n and the result of (7n - 5) divided by 2.
    
    Example Usage:
    assert is_nonagonal(10) == 325
    '''

    if not isinstance(n, int) or n <= 0:
        raise ValueError('n should be a positive integer')

    return n * (7*n - 5) / 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()