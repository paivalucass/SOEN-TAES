def surfacearea_cube(l):
    '''Calculate the surface area of a cube of a given size.'''
    return 6 * (l ** 2)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()