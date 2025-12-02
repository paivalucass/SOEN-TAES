def triangle_area(r) :
  '''Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.'''
  if r <= 0:
    return None
  
  area = 0.5 * r * r
  
  return area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5), 12.5)
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()