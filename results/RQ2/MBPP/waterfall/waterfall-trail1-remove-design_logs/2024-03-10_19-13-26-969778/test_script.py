def volume_cone(r, h):
    pi_value = 3.141592653589793
    if isinstance(r, (int, float)) and isinstance(h, (int, float)):
        if r > 0 and h > 0:
            return (1 / 3) * pi_value * (r ** 2) * h
        else:
            return "Invalid Input"
    else:
        return "Invalid Input"
import unittest
import math

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, delta=0.001)

if __name__ == '__main__':
    unittest.main()