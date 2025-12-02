def radian_degree(degree):
    return degree * (3.141592653589793 / 180)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()