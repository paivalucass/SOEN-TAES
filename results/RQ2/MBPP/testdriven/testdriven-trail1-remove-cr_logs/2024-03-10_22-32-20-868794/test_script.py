import math

def circle_circumference(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        return "Error or gracefully handled"
    return round(2 * math.pi * radius, 12)
import unittest
import math

class Test(unittest.TestCase):
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()