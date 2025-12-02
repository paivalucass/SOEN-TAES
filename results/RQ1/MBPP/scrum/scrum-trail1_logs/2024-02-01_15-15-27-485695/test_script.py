def square_Sum(n):
    '''Returns the sum of squares of the first n even natural numbers'''

    def validate_input(n):
        '''Validate input n to ensure it is a positive integer'''
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Input must be a positive integer")

    def calculate_square_sum(n):
        '''Calculate the sum of squares of the first n even natural numbers'''
        total = 0
        for i in range(1, n+1):
            total += (2*i)**2
        return total

    validate_input(n)
    return calculate_square_sum(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()