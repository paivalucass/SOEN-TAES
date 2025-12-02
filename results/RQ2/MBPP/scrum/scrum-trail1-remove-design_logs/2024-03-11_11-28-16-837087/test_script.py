import math

def circle_circumference(r):
    return 2 * math.pi * r

import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()