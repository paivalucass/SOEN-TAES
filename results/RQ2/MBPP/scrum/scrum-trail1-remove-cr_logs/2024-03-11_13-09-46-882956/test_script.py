def volume_cone(r, h):
    import math
    
    if r <= 0 or h <= 0 or not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        return "Error"
    
    volume = (1/3) * math.pi * r**2 * h
    return round(volume, 15) if volume != 0 else 0
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, places=3)

if __name__ == '__main__':
    unittest.main()