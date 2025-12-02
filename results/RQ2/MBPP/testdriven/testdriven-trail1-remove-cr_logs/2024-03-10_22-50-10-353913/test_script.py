import math

def lateralsurface_cone(radius, height):
    """
    Calculate the lateral surface area of a cone using the formula (π*r*sqrt(r^2+h^2)).
    
    Args:
    radius (float): The radius of the cone.
    height (float): The height of the cone.
    
    Returns:
    float: The calculated lateral surface area of the cone.
    
    Raises:
    ValueError: If the radius or height is a negative number.
    """
    # Validate input parameters
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative numbers.")
    
    # Calculate lateral surface area
    lateral_surface_area = math.pi * radius * math.sqrt(radius**2 + height**2)
    
    return lateral_surface_area

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654, places=10)

if __name__ == '__main__':
    unittest.main()