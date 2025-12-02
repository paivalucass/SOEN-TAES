def radian_degree(degree):
    import math

    try:
        if isinstance(degree, (int, float)):
            if -180 <= degree <= 180:
                return math.radians(degree)
            else:
                raise ValueError("Degree value must be within the range of -180 to 180 degrees")
        else:
            raise TypeError("Input must be a numeric value")
    except Exception as e:
        return str(e)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()