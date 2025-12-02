def square_perimeter(side_length):
    '''
    Write a function that returns the perimeter of a square given its side length as input.
    assert square_perimeter(10)==40
    '''
    if isinstance(side_length, (int, float)):
        if side_length > 0:
            return 4 * side_length
        else:
            return "Invalid input: Side length must be greater than 0"
    else:
        return "Invalid input: Side length must be a number"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()