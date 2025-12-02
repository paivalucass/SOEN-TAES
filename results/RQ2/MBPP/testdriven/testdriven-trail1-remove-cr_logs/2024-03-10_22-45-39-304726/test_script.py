import math

def surface_Area(b, s):
    '''Write a python function to find the surface area of a square pyramid with a given base edge and height.'''
    surface_area = b**2 + 2 * b * math.sqrt((b/2)**2 + s**2)
    return surface_area

# Assertion to validate the function's correctness
assert surface_Area(3, 4) == 33
import unittest

class Test(unittest.TestCase):
    def test_surface_area_calculation(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()