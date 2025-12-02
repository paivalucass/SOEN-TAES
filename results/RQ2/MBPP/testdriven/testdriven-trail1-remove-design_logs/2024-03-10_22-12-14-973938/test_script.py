def surface_Area(b, s):
    if not (isinstance(b, (int, float)) and isinstance(s, (int, float))):
        return "Error: Invalid input type"
    
    if b <= 0 or s <= 0:
        return "Error: Input should be positive"
    
    if b > 1000 or s > 1000:
        return "Error: Input out of range"
    
    base_area = b * b
    side_area = b * (2 * s)
    surface_area = base_area + side_area
    
    return surface_area
import unittest

class Test(unittest.TestCase):
    def test_surface_Area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()