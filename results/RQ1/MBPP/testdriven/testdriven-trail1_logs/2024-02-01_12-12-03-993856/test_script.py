import math
def area_polygon(num_sides, side_length):
    '''Write a function to calculate the area of a regular polygon given the length and number of its sides.'''
    if num_sides < 3 or side_length <= 0:
        raise ValueError("Number of sides should be 3 or more and length should be greater than 0.")
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    return area

# Test the function with different values
assert math.isclose(area_polygon(3, 0), 0.0, rel_tol=0.001)
assert math.isclose(area_polygon(4, 1), 1.0, rel_tol=0.001)
assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()