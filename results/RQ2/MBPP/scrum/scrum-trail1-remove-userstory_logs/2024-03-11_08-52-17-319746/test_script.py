def volume_sphere(r):
    '''Write a function to find the volume of a sphere.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    
    V = (4/3) * math.pi * r**3
    return V
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_sphere(10), 4188.790204786391, delta=0.001)

if __name__ == '__main__':
    unittest.main()