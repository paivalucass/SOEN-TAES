import math

def radian_degree(degree):
    try:
        radians = math.radians(float(degree))
        return round(radians, 14)
    except (ValueError, TypeError):
        return "Error message"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()