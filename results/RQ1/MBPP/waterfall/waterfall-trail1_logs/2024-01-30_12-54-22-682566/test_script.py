def volume_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid input: radius and height must be positive values"

    volume = math.pi * radius**2 * height
    return volume
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()