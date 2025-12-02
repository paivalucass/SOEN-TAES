import math

def surfacearea_sphere(r):
    '''
    Function to calculate the surface area of a sphere using the formula A = 4 * π * r^2
    Args:
        r: The radius of the sphere
    Returns:
        The surface area of the sphere
    Raises:
        ValueError if the radius is negative or non-numeric
    '''
    try:
        if r < 0 or not isinstance(r, (int, float)):
            raise ValueError("Radius must be a non-negative numeric value")
        return 4 * math.pi * r**2
    except ValueError as ve:
        return str(ve)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()