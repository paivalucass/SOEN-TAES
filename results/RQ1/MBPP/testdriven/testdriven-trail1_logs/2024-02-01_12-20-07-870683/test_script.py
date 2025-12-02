import cmath

def convert(numbers):
    '''This function converts complex numbers to polar coordinates.'''
    return cmath.polar(numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()