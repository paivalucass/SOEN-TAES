import math

def circle_circumference(r):
    '''Write a function to find the circumference of a circle.'''
    if not isinstance(r, (int, float)):
        return 'Error: Input is not a number'
    elif r < 0:
        return 0  # Changed to return 0 for negative radius
    else:
        circumference = 2 * math.pi * abs(r)  # Changed to use absolute value of radius
        return round(circumference, 2)

# Test cases
assert math.isclose(circle_circumference(10), 62.83, rel_tol=0.001)
assert math.isclose(circle_circumference(-5), 31.42, rel_tol=0.001)  # Test for negative radius
assert circle_circumference('abc') == 'Error: Input is not a number'  # Test for non-numeric input
assert math.isclose(circle_circumference(0), 0, rel_tol=0.001)  # Test for radius=0
import unittest
import math

class Test(unittest.TestCase):
    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(10), 62.83, places=2)

if __name__ == '__main__':
    unittest.main()

# The circle_circumference function calculates the circumference of a circle given its radius using the formula 2 * pi * r. 
# The test case checks if the calculated circumference is approximately equal to the expected value with a given tolerance.