import math
def triangle_area(r) :
    '''Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.'''
    if r < 0:
        return None
    return (r**2 * math.sqrt(3)) / 4
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(3), 4.5)

if __name__ == '__main__':
    unittest.main()