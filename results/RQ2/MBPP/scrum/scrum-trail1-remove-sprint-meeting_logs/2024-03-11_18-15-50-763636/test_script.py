def volume_sphere(r):
    if not isinstance(r, (int, float)):
        return "Error: Radius must be a numeric value"
    if r <= 0:
        return "Error: Radius must be a positive value"
    
    volume = (4/3) * math.pi * (r ** 3)
    return volume
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_sphere(10), 4188.790204786391, delta=0.001)

if __name__ == '__main__':
    unittest.main()