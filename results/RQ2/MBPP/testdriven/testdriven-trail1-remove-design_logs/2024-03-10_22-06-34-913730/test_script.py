def minimum(a, b):
    '''Write a python function to find the minimum of two numbers.
    This function handles the case when both a and b are None
    by raising a ValueError.
    Parameters:
    - a: first number
    - b: second number
    Returns:
    - The minimum of a and b
    '''
    if a is None or b is None:
        raise ValueError("Both a and b cannot be None")
    return min(a, b)
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()