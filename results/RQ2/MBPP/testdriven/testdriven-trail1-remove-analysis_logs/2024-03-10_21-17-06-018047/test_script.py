def volume_cone(radius, height):
    '''
    Write a function to find the volume of a cone.
    assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
    '''
    import math
    
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    else:
        volume = (1/3) * math.pi * (radius**2) * height
        return volume
import unittest
import math

class Test(unittest.TestCase):
    def test_volume_cone(self):
        self.assertAlmostEqual(volume_cone(5, 12), 314.15926535897927, places=3)

if __name__ == '__main__':
    unittest.main()