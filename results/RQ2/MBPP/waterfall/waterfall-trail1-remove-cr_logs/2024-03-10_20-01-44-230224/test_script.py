def volume_cone(radius, height):
    import math
    if radius <= 0 or height <= 0:
        return "Invalid input"
    volume = (1/3) * math.pi * radius**2 * height
    return round(volume, 3)
import math
import unittest

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, places=3)

if __name__ == '__main__':
    unittest.main()