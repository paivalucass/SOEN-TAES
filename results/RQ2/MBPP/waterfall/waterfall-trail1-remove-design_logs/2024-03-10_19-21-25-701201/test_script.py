import math

def radian_degree(degree):
    try:
        radian = degree * (math.pi / 180)
        return round(radian, 15)
    except (TypeError, ValueError):
        return "Error"

import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()