import math
def lateral_surface_cylinder(r, h):
    """
    Calculate the lateral surface area of a cylinder
    :param r: radius of the cylinder
    :param h: height of the cylinder
    :return: lateral surface area of the cylinder
    """
    if isinstance(r, (int, float)) and isinstance(h, (int, float)):
        if r >= 0 and h >= 0:
            return 2 * math.pi * r * h
        else:
            return 0
    else:
        return "Error: Invalid input"

# test
assert math.isclose(lateral_surface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15, delta=0.001)

if __name__ == '__main__':
    unittest.main()