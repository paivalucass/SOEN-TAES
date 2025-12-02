def surfacearea_sphere(radius):
    ''' 
    Write a function to find the surface area of a sphere.
    This function calculates the surface area of a sphere using the given radius.
    '''
    
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a numeric value")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    surface_area = 4 * math.pi * (radius**2)
    
    return surface_area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, places=3)

if __name__ == '__main__':
    unittest.main()