def jacobsthal_num(n):
    '''
    This function finds the nth Jacobsthal number.
    Jacobsthal numbers are a sequence of numbers where each number is twice the previous number plus the one before that.
    For example, the 5th Jacobsthal number is 11.

    Args:
    n: an integer representing the position of the Jacobsthal number to be found
    
    Returns:
    The nth Jacobsthal number
    '''

    memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]
    else:
        memo[n] = jacobsthal_num(n-1) + 2*jacobsthal_num(n-2)
        return memo[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()