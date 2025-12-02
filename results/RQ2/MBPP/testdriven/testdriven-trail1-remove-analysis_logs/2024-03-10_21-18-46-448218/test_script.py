def cube_Sum(n):
    ''' 
    Write a python function to find the cube sum of the first n even natural numbers.
    assert cube_Sum(2) == 72
    '''
    cube_sum_of_even_numbers = 0
    for i in range(1, n+1):
        cube_sum_of_even_numbers += (2*i)**3
    return cube_sum_of_even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()