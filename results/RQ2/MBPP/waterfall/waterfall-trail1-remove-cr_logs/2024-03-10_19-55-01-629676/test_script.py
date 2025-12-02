import math

def circle_circumference(radius, rel_tol=10e-9):
    if radius < 0:
        return 'Invalid Input'
    circumference = 2 * math.pi * radius
    return round(circumference, 2)
import unittest
import math

class Test(unittest.TestCase):
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()