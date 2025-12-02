import math

def radian_degree(degree):
    try:
        if not isinstance(degree, (int, float)):
            raise ValueError("Degree must be a valid number")
        
        radians = math.radians(degree)
        return radians
    except Exception as e:
        return "Error: Invalid degree value"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(radian_degree(90), 1.5707963267948966)

if __name__ == '__main__':
    unittest.main()