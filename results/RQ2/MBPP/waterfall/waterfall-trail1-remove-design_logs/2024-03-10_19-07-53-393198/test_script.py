import math

def circle_circumference(r):
    if isinstance(r, (int, float)):
        if r <= 0:
            return "Invalid input"
        return round(2 * math.pi * r, 2)
    else:
        return "Invalid input"
import unittest
import math

class Test(unittest.TestCase):
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()