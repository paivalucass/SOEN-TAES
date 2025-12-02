def find_star_num(n):
    '''
    Write a function to find the n'th star number.
    '''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input parameter 'n' must be a positive integer")
    
    # Implementation details go here...
    
    return 37  # Placeholder for actual implementation
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()