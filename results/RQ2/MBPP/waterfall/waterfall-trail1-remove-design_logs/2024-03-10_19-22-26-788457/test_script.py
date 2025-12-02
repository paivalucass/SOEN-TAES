def triangle_area(r) :
    '''Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.'''
    if type(r) not in [int, float]:
        return None
    elif r <= 0:
        return None
    else:
        return (0.5 * r * r)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), 0.5)
        self.assertEqual(triangle_area(2), 2)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()