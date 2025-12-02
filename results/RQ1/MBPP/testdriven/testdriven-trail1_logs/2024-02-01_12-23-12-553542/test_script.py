def square_Sum(n):  
    '''Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
    assert square_Sum(2) == 10'''
    if not isinstance(n, int):
        raise TypeError("Input n must be an integer")
    if n <= 0:
        return 0
    # Generate list of first n odd natural numbers
    odd_numbers = [i for i in range(1, 2*n, 2)]
    # Calculate sum of squares
    sum_of_squares = sum(x**2 for x in odd_numbers)
    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()