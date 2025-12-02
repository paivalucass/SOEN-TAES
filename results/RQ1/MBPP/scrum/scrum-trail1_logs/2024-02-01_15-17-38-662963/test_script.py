def otherside_rightangle(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive numbers")
    return (a**2 + b**2)**0.5
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()