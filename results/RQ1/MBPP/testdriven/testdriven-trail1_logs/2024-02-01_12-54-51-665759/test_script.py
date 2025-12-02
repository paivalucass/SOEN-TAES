def difference(n):
    '''Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.'''
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    # Calculate sum of cubes
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    
    # Calculate sum of natural numbers
    sum_of_natural_numbers = sum([i for i in range(1, n+1)])
    
    return sum_of_cubes - sum_of_natural_numbers

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()