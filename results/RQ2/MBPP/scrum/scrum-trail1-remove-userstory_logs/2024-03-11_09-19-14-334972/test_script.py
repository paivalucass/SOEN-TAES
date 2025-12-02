import math

def radian_degree(degree):
    try:
        radians = math.radians(degree)
        return round(radians, 16)
    except TypeError:
        return "Error: Invalid input"
    except Exception as e:
        return "Error: " + str(e)

import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()