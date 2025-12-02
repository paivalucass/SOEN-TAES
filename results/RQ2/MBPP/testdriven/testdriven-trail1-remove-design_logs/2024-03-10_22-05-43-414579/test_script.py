def volume_cone(r, h):
    import math
    if r <= 0 or h <= 0:
        return 0
    elif r < 0 or h < 0:
        return "Error: Invalid input"
    else:
        return (1/3) * math.pi * (r**2) * h
import unittest
import math

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, delta=0.001)

if __name__ == '__main__':
    unittest.main()