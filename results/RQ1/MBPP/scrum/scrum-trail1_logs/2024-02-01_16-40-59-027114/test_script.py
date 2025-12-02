def area_tetrahedron(side):
    '''Write a function to calculate the area of a tetrahedron.'''
    return (side ** 2) * (3 ** 0.5)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()