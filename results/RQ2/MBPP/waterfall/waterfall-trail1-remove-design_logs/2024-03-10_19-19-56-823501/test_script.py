import math

def surface_Area(base_length, side_length):
    if base_length <= 0 or side_length <= 0:
        raise ValueError("Base length and side length must be greater than 0")
    
    slant_height = math.sqrt((base_length/2)**2 + side_length**2)
    return base_length*base_length + 2*base_length*slant_height
import unittest

class Test(unittest.TestCase):
    def test_surface_area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()