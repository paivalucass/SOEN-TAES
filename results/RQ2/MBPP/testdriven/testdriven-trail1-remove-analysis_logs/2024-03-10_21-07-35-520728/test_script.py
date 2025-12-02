def square_perimeter(a):
    '''
    Write a function that returns the perimeter of a square given its side length as input.
    assert square_perimeter(10)==40
    '''
    if isinstance(a, (int, float)):
        perimeter = 4 * a
        return perimeter
    else:
        return "Invalid input for side length of the square"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()