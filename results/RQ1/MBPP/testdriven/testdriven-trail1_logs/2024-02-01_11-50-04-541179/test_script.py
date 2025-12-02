def square_perimeter(side_length):
    '''This function calculates the perimeter of a square given its side length as input.'''
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("Input must be a non-negative number")
    perimeter = side_length * 4
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()