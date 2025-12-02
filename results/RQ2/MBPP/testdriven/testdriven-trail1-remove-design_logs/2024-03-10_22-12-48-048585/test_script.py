def polar_rect(x, y):
    import cmath
    import math
    
    if x <= 0 or y <= 0:
        return "Error: Invalid input"
    
    radius = math.sqrt(x**2 + y**2)
    angle = math.atan2(y, x)
    rectangular_coords = (radius, angle)
    rectangular_complex = cmath.rect(radius, angle)
    
    return rectangular_coords, rectangular_complex

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2 + 2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()