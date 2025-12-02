from math import sqrt

def area_tetrahedron(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    
    area = (side * side) * sqrt(3)
    return round(area, 14)
import unittest

class Test(unittest.TestCase):
    def test_area_tetrahedron(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()