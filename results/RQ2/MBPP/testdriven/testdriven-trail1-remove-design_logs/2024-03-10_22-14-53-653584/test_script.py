import math

def triangle_area(r) :
    '''
    Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
    assert triangle_area(-1) == None
    '''

    # input validation
    if not isinstance(r, (int, float)) or r < 0 :
        return None
    
    # calculation of area
    else:
        return (math.pi * r * r) / 2
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), math.pi / 2)
        self.assertEqual(triangle_area(2), 2 * math.pi)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()