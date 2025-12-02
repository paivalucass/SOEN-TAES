def triangle_area(r) :
    '''
    Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
    assert triangle_area(-1) == None
    '''

    if r <= 0:
        return None
    else:
        base = 2 * r
        radius_squared = r ** 2
        height = (radius_squared - (0.5 * r ** 2)) ** 0.5
        area = 0.5 * base * height
        return area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(3), 7.0685834705770345)
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()