def sector_area(r, a):
    '''Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.'''
    if a > 360:
        return None
    else:
        return (0.5 * r * r * (a * 3.14159 / 180))
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sector_area(4, 45), 6.283185307179586)

if __name__ == '__main__':
    unittest.main()