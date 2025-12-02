def square_Sum(n):
    """
    This function takes in an integer n and returns the sum of squares of the first n even natural numbers.
    """
    if n <= 0:
        return 0

    sum_of_squares = 0
    for num in range(1, n+1):
        even_number = 2 * num
        sum_of_squares += even_number ** 2

    return sum_of_squares

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()