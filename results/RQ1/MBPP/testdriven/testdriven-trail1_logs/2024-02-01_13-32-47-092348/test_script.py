def test_three_equal(x, y, z):
    '''Write a python function to count the number of equal numbers from three given integers.'''
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise ValueError("Inputs must be integers")

    if x == y == z:
        return 3
    elif x != y and y != z and z != x:
        return 0
    else:
        return 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()