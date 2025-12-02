def maximum(a, b):
    '''
    Finds the maximum of two numbers.
    
    Args:
    a: int or float, the first number
    b: int or float, the second number
    
    Returns:
    int or float, the maximum of the two numbers
    '''

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both input parameters must be numeric")
    
    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()