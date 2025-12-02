def volume_cylinder(radius, height):
    import math
    if type(radius) != int or type(height) != int:
        return "Invalid input: Radius and height must be numbers"
    elif radius <= 0 or height <= 0:
        return "Invalid input: Radius and height must be positive numbers"
    else:
        volume = math.pi * (radius ** 2) * height
        return volume
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()