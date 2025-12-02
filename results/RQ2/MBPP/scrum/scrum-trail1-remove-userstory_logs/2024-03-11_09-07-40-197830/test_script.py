def volume_cone(r, h):
    import math

    if type(r) not in (int, float) or type(h) not in (int, float):
        return "Error: radius and height must be numeric"
    elif r <= 0 or h <= 0:
        return "Error: radius and height must be positive numbers"
    else:
        volume = (1/3) * math.pi * (r**2) * h
        return round(volume, 3) # Round off to 3 decimal places
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()