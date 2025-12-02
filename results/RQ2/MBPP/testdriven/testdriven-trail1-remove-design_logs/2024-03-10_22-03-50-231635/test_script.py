def volume_cylinder(r, h):
    import math

    if r <= 0 or h <= 0:
        return "Error: Invalid input. Radius and height must be positive values."

    if not (isinstance(r, (int, float)) and isinstance(h, (int, float))):
        return "Error: Invalid input. Radius and height must be numeric values."

    volume = math.pi * (r ** 2) * h
    return round(volume, 1)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()