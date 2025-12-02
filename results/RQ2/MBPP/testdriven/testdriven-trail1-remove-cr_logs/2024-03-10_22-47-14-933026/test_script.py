def radian_degree(degree):
    try:
        if degree < 0 or degree > 360:
            raise ValueError("Input degree must be within the valid range of 0 to 360 degrees")
            
        # Convert degree to radians using the formula: radians = degrees * (pi/180)
        radians = degree * (3.14159265358979323846/180)

        return radians

    except ValueError as e:
        print(e)
        # Handle the error or pass it to the caller
        # For testing purposes, return None or raise the error

assert radian_degree(90)==1.5707963267948966
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(radian_degree(90), 1.5707963267948966, places=15)

if __name__ == '__main__':
    unittest.main()