def volume_cube(l):
    '''Write a function to find the volume of a cube given its side length.'''
    return l ** 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()