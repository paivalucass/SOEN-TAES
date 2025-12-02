import math

def circle_circumference(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    circumference = 2 * math.pi * r
    return round(circumference, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()