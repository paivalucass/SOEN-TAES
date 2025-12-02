def area_tetrahedron(side):
    '''Write a function to calculate the area of a tetrahedron.'''
    height = (6 ** 0.5 / 3) * side
    triangular_area = (side ** 2) * (3 ** 0.5 / 4)
    area = 4 * triangular_area
    return area

# Write test cases
assert area_tetrahedron(3) == 15.588457268119894
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()