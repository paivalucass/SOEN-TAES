def sector_area(r, a):
    if not isinstance(r, (int, float)) or not isinstance(a, (int, float)):
        return "Error message"

    if r <= 0 or a <= 0:
        return "Radius and angle should be positive numbers"

    if a > 360:
        return None

    return 0.5 * r**2 * (a/360*2*3.141592653589793)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()