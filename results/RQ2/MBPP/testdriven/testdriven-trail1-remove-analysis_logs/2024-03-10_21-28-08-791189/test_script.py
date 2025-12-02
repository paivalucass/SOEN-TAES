def sector_area(r, a):
    import math  # Moved the import statement to the beginning of the code for better organization
    '''Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.'''
    if r < 0 or a < 0 or a > 360:  # Removed the unnecessary try-except block as it does not provide any specific error handling and may suppress useful error messages
        return None
    else:
        return (0.5 * r**2 * (math.radians(a)))  # Added comments to explain the purpose of the function and the parameters.
import unittest

class Test(unittest.TestCase):
    def test_sector_area(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)
        self.assertIsNone(sector_area(4, 400))

if __name__ == '__main__':
    unittest.main()