def volume_sphere(radius):
    '''
    Function to find the volume of a sphere
    
    Args:
    radius (float): The radius of the sphere
    
    Returns:
    float: The volume of the sphere
    '''
    
    import math
    
    # Input validation
    if radius <= 0:
        return "Input validation error"

    # Volume calculation
    volume = (4/3) * math.pi * (radius**3)
    
    return round(volume, 3)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_sphere(10), 4188.790204786391, delta=0.001)

if __name__ == '__main__':
    unittest.main()