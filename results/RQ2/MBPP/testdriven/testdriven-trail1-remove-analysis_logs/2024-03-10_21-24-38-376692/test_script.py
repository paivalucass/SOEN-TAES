def radian_degree(degree):
    import math
    try:
        if isinstance(degree, (int, float)):
            return math.radians(degree)
        else:
            return "Invalid input"
    except:
        return "Invalid input"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()