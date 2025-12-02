def volume_cone(r, h):
    import math
    if not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        return "ValueError"
    elif r <= 0 or h <= 0:
        return "Invalid input: both radius and height must be positive numbers"
    else:
        volume = (1/3) * math.pi * (r**2) * h
        return volume
import unittest
import math

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, places=3)

if __name__ == '__main__':
    unittest.main()