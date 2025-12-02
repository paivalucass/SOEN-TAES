def is_octagonal(n):
    '''Write a function to find the nth octagonal number.'''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Calculate the nth octagonal number
    result = n * (3 * n - 2)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()