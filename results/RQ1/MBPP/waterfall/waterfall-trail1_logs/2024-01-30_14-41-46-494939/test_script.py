def surfacearea_cylinder(radius: float, height: float) -> float:
    if radius <= 0 or height <= 0:
        return "Error: Invalid input"
    else:
        return round(2 * 3.14159 * radius * (radius + height), 2)

import math
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cylinder(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.4777960769379)

if __name__ == '__main__':
    unittest.main()