def median_trapezium(base1, base2, height):
    '''Write a function to find the median length of a trapezium.'''
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError
    return (base1 + base2) / 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()