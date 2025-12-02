def validate_input(n):
    if n < 0 or type(n) != int:
        raise ValueError("Input must be a non-negative integer")

def square_Sum(n):
    try:
        validate_input(n)
        odd_numbers = (i for i in range(1, 2*n, 2))
        sum_of_squares = sum(x**2 for x in odd_numbers)
        return sum_of_squares
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()