def square_sum_of_first_n_odd_numbers(n):
    '''
    This function takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
    '''
    sum_of_squares = sum(i*i for i in range(1, 2*n+1, 2))
    return sum_of_squares

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()