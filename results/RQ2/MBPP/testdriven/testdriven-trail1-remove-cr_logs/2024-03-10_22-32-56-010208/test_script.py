import math

def area_polygon(s, l):
    '''Write a function to calculate the area of a regular polygon given the length and number of its sides.'''
    if s < 3 or l <= 0:
        raise ValueError("Invalid input values")
    
    apothem = l / (2 * math.tan(math.pi / s))
    area = (s * l * apothem) / 2
    return area
assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()