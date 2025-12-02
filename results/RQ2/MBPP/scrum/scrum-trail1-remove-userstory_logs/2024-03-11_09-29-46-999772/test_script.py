def test_three_equal(x, y, z):
    '''Write a python function to count the number of equal numbers from three given integers.'''
    if x == y == z:
        return 3
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()