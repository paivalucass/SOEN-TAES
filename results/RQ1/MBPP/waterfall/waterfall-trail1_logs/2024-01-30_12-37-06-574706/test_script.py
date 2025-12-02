import math

def circle_circumference(radius):
    '''Write a function to find the circumference of a circle'''
    
    # Validate input for negative values
    if not isinstance(radius, (int, float)) or radius < 0:
        return "Invalid input"

    # Calculate circumference using the math module
    circumference = 2 * math.pi * radius
    return round(circumference, 3)

import unittest
import math

class Test(unittest.TestCase):
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(10), 62.830000000000005, delta=0.001)

if __name__ == '__main__':
    unittest.main()